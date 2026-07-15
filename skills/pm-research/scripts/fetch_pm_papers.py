#!/usr/bin/env python3
"""Batch search and download Process Mining papers from ArXiv and Semantic Scholar.

Usage:
    python3 fetch_pm_papers.py --keywords "process mining,conformance checking" --since-year 2025 --max-papers 20

Outputs structured JSON on stdout with download results.
Does NOT handle IEEE Xplore (requires browser) or Synthadoc ingestion (MCP tool).

Relevance filtering (v0.3.0):
  Each paper title+abstract is checked for PM relevance BEFORE download and synthadoc ingestion.
  - LLM mode: uses OPENROUTER_API_KEY env var (requires owner grant).
  - Rule-based fallback: keyword scoring when no API key available.
  - Use --no-relevance-check to skip.
  Filtered papers appear in results["filtered_out"] and are NOT downloaded.
"""

import sys
import argparse
import json
import os
import re
import time
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path


ARXIV_API = "http://export.arxiv.org/api/query"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
PDF_MAGIC = b"%PDF"
RATE_LIMIT_DELAY = 1.5

DEFAULT_KEYWORDS = [
    "process mining", "process discovery", "conformance checking",
    "process enhancement", "process model", "task mining",
    "event logs", "audit trail", "audit log analysis",
    "process monitoring", "process compliance", "continuous auditing",
    "internal audit", "deviation analysis", "compliance monitoring",
    "process mining banking", "financial auditing",
]

# ── Relevance filter ───────────────────────────────────────────────────────────

_PM_STRONG = [
    r"\bprocess mining\b",
    r"\bprocess discovery\b",
    r"\bconformance checking\b",
    r"\bevent log[s]?\b",
    r"\bevent stream[s]?\b",
    r"\bpetri net[s]?\b",
    r"\balpha[+*]? (miner|algorithm)\b",
    r"\binductive miner\b",
    r"\bheuristic miner\b",
    r"\bfuzzy miner\b",
    r"\bsplit miner\b",
    r"\btrace[s]? alignment\b",
    r"\bprocess enhancement\b",
    r"\bprocess monitoring\b",
    r"\bprocess compliance\b",
    r"\bdeclare (model|constraint|miner)\b",
    r"\bbpmn (mining|model|process)\b",
    r"\bworkflow (net|mining|model)\b",
    r"\bpm4py\b",
    r"\bdrift detect\w* (in|for)? process\b",
    r"\btask mining\b",
    r"\bobject.centric process\b",
    r"\baudit trail[s]?\b",
    r"\bprocess variant[s]?\b",
]

_PM_WEAK = [
    r"\bbusiness process[es]?\b",
    r"\bevent data\b",
    r"\bprocess analysis\b",
    r"\bworkflow[s]?\b",
    r"\bcase[s]? id\b",
    r"\bactivity (sequence|execution|log)\b",
    r"\bprocess instance[s]?\b",
    r"\bprocess tree[s]?\b",
    r"\bbpm\b",
    r"\bprocess aware\b",
]

_NON_PM_STRONG = [
    r"\bimage (classification|recognition|segmentation|generation)\b",
    r"\bobject detection\b",
    r"\bspeech recognition\b",
    r"\bmachine translation\b",
    r"\brecommendation system[s]?\b",
    r"\bdrug (discovery|design|synthesis)\b",
    r"\bprotein (folding|structure)\b",
    r"\bgenome\b",
    r"\bclinical trial[s]?\b(?!.*process)",
    r"\bmedical image[s]?\b",
    r"\bautonomous (driving|vehicle)\b",
    r"\brobotic[s]?\b(?!.*process)",
    r"\bcryptograph\w+\b",
    r"\bblockchain\b(?!.*process)",
    r"\bsentiment analysis\b",
]


def _rule_based_relevance(abstract, title):
    text = (title + " " + abstract).lower()
    strong_hits = [p for p in _PM_STRONG if re.search(p, text, re.IGNORECASE)]
    weak_hits = [p for p in _PM_WEAK if re.search(p, text, re.IGNORECASE)]
    neg_hits = [p for p in _NON_PM_STRONG if re.search(p, text, re.IGNORECASE)]

    if strong_hits:
        if len(neg_hits) >= 3 and len(strong_hits) < 2:
            return {"relevant": False, "method": "rule_based",
                    "reason": "Strong PM term but dominated by non-PM signals"}
        return {"relevant": True, "method": "rule_based",
                "reason": "Strong PM signals found"}
    elif len(weak_hits) >= 2 and not neg_hits:
        return {"relevant": True, "method": "rule_based",
                "reason": "Multiple weak PM signals, no counter-signals"}
    elif neg_hits and not strong_hits:
        return {"relevant": False, "method": "rule_based",
                "reason": "Non-PM domain signals detected"}
    else:
        return {"relevant": True, "method": "rule_based",
                "reason": "Ambiguous abstract — keeping to avoid false negative"}


def _llm_relevance_batch(papers, api_key, model="google/gemini-2.0-flash-001"):
    items = []
    for i, p in enumerate(papers):
        abstract = (p.get("abstract") or "").strip()[:400]
        title = (p.get("title") or "").strip()
        items.append(f"[{i}] Title: {title}\nAbstract: {abstract}")

    system_prompt = (
        "You are a Process Mining research classifier. "
        "Decide if each paper is directly relevant to Process Mining (event log analysis, "
        "process discovery, conformance checking, process enhancement, workflow mining, "
        "trace alignment, Petri nets in process analysis, object-centric process mining). "
        "Not relevant: general ML/AI, NLP, computer vision, drug discovery, genomics. "
        'Respond ONLY with JSON array: [{"index": int, "relevant": bool, "reason": "one sentence"}]. '
        "No markdown."
    )

    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Classify {len(papers)} papers:\n\n" + "\n\n".join(items)},
        ],
        "max_tokens": 512,
        "temperature": 0.0,
    }).encode("utf-8")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/ouroboros",
        "X-Title": "pm-research skill",
    }

    try:
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=payload, headers=headers, method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
        content = result["choices"][0]["message"]["content"].strip()
        if content.startswith("```"):
            content = re.sub(r"^```[a-z]*\n?", "", content)
            content = re.sub(r"\n?```$", "", content)
        verdicts = json.loads(content)
        out = []
        for v in verdicts:
            idx = v.get("index", -1)
            if 0 <= idx < len(papers):
                out.append({
                    "id": papers[idx].get("id", ""),
                    "relevant": bool(v.get("relevant", True)),
                    "reason": str(v.get("reason", "")),
                    "method": "llm",
                })
        return out
    except Exception as e:
        return [{"id": p.get("id", ""), "error": str(e)} for p in papers]


def check_relevance(papers, use_llm=True, llm_batch_size=10):
    """Annotate papers with PM relevance. Runs BEFORE download and synthadoc ingestion."""
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    use_llm = use_llm and bool(api_key)

    if use_llm:
        print(f"Relevance: LLM via OpenRouter ({len(papers)} papers)...", file=sys.stderr)
    else:
        reason = "no OPENROUTER_API_KEY" if not api_key else "use_llm=False"
        print(f"Relevance: rule-based filter ({reason}).", file=sys.stderr)

    annotated = []
    if use_llm:
        verdicts_map = {}
        for start in range(0, len(papers), llm_batch_size):
            batch = papers[start:start + llm_batch_size]
            for v in _llm_relevance_batch(batch, api_key):
                if "error" not in v:
                    verdicts_map[v["id"]] = v
            time.sleep(0.5)
        for p in papers:
            p2 = dict(p)
            pid = p.get("id", "")
            if pid in verdicts_map:
                v = verdicts_map[pid]
                p2["relevant"] = v["relevant"]
                p2["relevance_reason"] = v["reason"]
                p2["relevance_method"] = "llm"
            else:
                rb = _rule_based_relevance(p.get("abstract", ""), p.get("title", ""))
                p2["relevant"] = rb["relevant"]
                p2["relevance_reason"] = rb["reason"] + " [llm_failed_fallback]"
                p2["relevance_method"] = "rule_based_fallback"
            annotated.append(p2)
    else:
        for p in papers:
            rb = _rule_based_relevance(p.get("abstract", ""), p.get("title", ""))
            p2 = dict(p)
            p2["relevant"] = rb["relevant"]
            p2["relevance_reason"] = rb["reason"]
            p2["relevance_method"] = "rule_based"
            annotated.append(p2)
    return annotated


# ── HTTP helpers ───────────────────────────────────────────────────────────────

def http_get(url, headers=None, timeout=30):
    hdrs = {"User-Agent": USER_AGENT}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def is_valid_pdf(data):
    return len(data) >= 4 and data[:4] == PDF_MAGIC


def safe_filename(name, max_len=50):
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s]+", "_", name.strip())
    return name[:max_len]


# ── Search ─────────────────────────────────────────────────────────────────────

def search_arxiv(keywords, since_year, max_results=20):
    query = " AND ".join('all:"' + kw + '"' for kw in keywords)
    url = (ARXIV_API + "?search_query=" + urllib.request.quote(query)
           + "&sortBy=submittedDate&sortOrder=descending&max_results=" + str(max_results))
    try:
        data = http_get(url)
        root = ET.fromstring(data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        papers = []
        for entry in root.findall("atom:entry", ns):
            title_el = entry.find("atom:title", ns)
            id_el = entry.find("atom:id", ns)
            summary_el = entry.find("atom:summary", ns)
            if title_el is None or id_el is None:
                continue
            arxiv_id = id_el.text.strip().split("/abs/")[-1]
            title = title_el.text.strip().replace("\n", " ")
            abstract = summary_el.text.strip() if summary_el is not None else ""
            pdf_url = "https://arxiv.org/pdf/" + arxiv_id + ".pdf"
            id_match = re.match(r"(\d{2})\d{2}\.", arxiv_id)
            year = 2000 + int(id_match.group(1)) if id_match else 0
            if year < since_year:
                continue
            papers.append({
                "source": "arxiv", "id": arxiv_id, "title": title,
                "abstract": abstract[:500], "pdf_url": pdf_url, "year": year,
                "filename": arxiv_id + "_" + safe_filename(title) + ".pdf",
            })
        return papers
    except Exception as e:
        return [{"source": "arxiv", "error": str(e)}]


def search_arxiv_per_keyword(keywords, since_year, max_per_kw=10):
    all_papers = []
    seen_ids = set()
    for kw in keywords:
        try:
            for p in search_arxiv([kw], since_year, max_results=max_per_kw):
                if "error" in p:
                    all_papers.append(p)
                elif p["id"] not in seen_ids:
                    seen_ids.add(p["id"])
                    all_papers.append(p)
            time.sleep(RATE_LIMIT_DELAY)
        except Exception as e:
            all_papers.append({"source": "arxiv", "error": "keyword " + kw + ": " + str(e)})
    return all_papers


def search_semantic_scholar(keywords, since_year, max_results=20):
    query = " ".join(keywords)
    url = (SEMANTIC_SCHOLAR_API + "?query=" + urllib.request.quote(query)
           + "&year=" + str(since_year) + "-2026&fieldsOfStudy=Computer+Science"
           + "&limit=" + str(max_results)
           + "&fields=title,externalIds,openAccessPdf,abstract,year")
    try:
        data = http_get(url)
        result = json.loads(data)
        papers = []
        for item in result.get("data", []):
            oa = item.get("openAccessPdf")
            if not oa or not oa.get("url"):
                continue
            ext_ids = item.get("externalIds", {})
            arxiv_id = ext_ids.get("ArXiv")
            title = item.get("title", "Untitled")
            corpus_id = str(ext_ids.get("CorpusId", "x"))
            papers.append({
                "source": "semantic_scholar",
                "id": arxiv_id or corpus_id, "title": title,
                "abstract": (item.get("abstract") or "")[:500],
                "pdf_url": oa["url"], "year": item.get("year", 0),
                "filename": (arxiv_id or "ss_" + corpus_id) + "_" + safe_filename(title) + ".pdf",
                "is_arxiv": arxiv_id is not None,
            })
        return papers
    except urllib.error.HTTPError as e:
        code = e.code
        return [{"source": "semantic_scholar", "error": "403 Forbidden" if code == 403 else f"HTTP {code}"}]
    except Exception as e:
        return [{"source": "semantic_scholar", "error": str(e)}]


# ── Download ───────────────────────────────────────────────────────────────────

def download_pdf(paper, output_dir):
    source = paper.get("source", "unknown")
    source_dir = output_dir / (source + "_pdfs")
    source_dir.mkdir(parents=True, exist_ok=True)
    filepath = source_dir / paper["filename"]
    if filepath.exists():
        try:
            with open(filepath, "rb") as f:
                if is_valid_pdf(f.read(4)):
                    return {"status": "exists", "path": str(filepath), "paper": paper}
        except Exception:
            pass
    try:
        data = http_get(paper["pdf_url"])
        if not is_valid_pdf(data[:4]):
            return {"status": "paywall", "paper": paper}
        with open(filepath, "wb") as f:
            f.write(data)
        return {"status": "downloaded", "path": str(filepath), "paper": paper}
    except Exception as e:
        return {"status": "error", "error": str(e), "paper": paper}


def deduplicate(papers, output_dir):
    result = []
    for p in papers:
        if "error" in p:
            result.append(p)
            continue
        filepath = output_dir / (p.get("source", "unknown") + "_pdfs") / p["filename"]
        if not filepath.exists():
            result.append(p)
    return result


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch PM research papers")
    parser.add_argument("--keywords", default=",".join(DEFAULT_KEYWORDS))
    parser.add_argument("--since-year", type=int, default=2025)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--max-papers", type=int, default=20)
    parser.add_argument("--sources", default="arxiv,semantic_scholar")
    parser.add_argument("--no-relevance-check", action="store_true", default=False,
                        help="Skip relevance filtering — download all found papers")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    if args.output_dir is not None:
        output_dir = Path(args.output_dir)
    elif "OUROBOROS_SKILL_STATE_DIR" in os.environ:
        output_dir = Path(os.environ["OUROBOROS_SKILL_STATE_DIR"]) / "downloads"
    else:
        print(json.dumps({"error": "OUROBOROS_SKILL_STATE_DIR not set and --output-dir not provided."}),
              file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    sources = [s.strip() for s in args.sources.split(",")]

    results = {"papers_found": [], "filtered_out": [], "downloads": [], "errors": [], "summary": {}}

    # Search
    if "arxiv" in sources:
        print(f"Searching ArXiv ({len(keywords)} keywords, since {args.since_year})...", file=sys.stderr)
        all_papers = list(search_arxiv_per_keyword(keywords, args.since_year, max_per_kw=10))
    else:
        all_papers = []

    if "semantic_scholar" in sources:
        print("Searching Semantic Scholar...", file=sys.stderr)
        all_papers.extend(search_semantic_scholar(keywords, args.since_year, max_results=args.max_papers))
        time.sleep(RATE_LIMIT_DELAY)

    for p in all_papers:
        (results["errors"] if "error" in p else results["papers_found"]).append(p)

    # Deduplication
    seen, unique = set(), []
    for p in results["papers_found"]:
        pid = p.get("id", "")
        if pid not in seen:
            seen.add(pid)
            unique.append(p)
    results["papers_found"] = unique
    print(f"Found {len(results['papers_found'])} unique papers.", file=sys.stderr)

    # Relevance filter — BEFORE download and synthadoc
    if not args.no_relevance_check and results["papers_found"]:
        annotated = check_relevance(results["papers_found"], use_llm=True)
        relevant = [p for p in annotated if p.get("relevant", True)]
        filtered = [p for p in annotated if not p.get("relevant", True)]
        results["papers_found"] = relevant
        results["filtered_out"] = filtered
        if filtered:
            print(f"Relevance: {len(relevant)} kept, {len(filtered)} filtered out.", file=sys.stderr)
            for p in filtered:
                print(f"  FILTERED: {p.get('title', '?')[:70]} — {p.get('relevance_reason', '')}", file=sys.stderr)
    elif args.no_relevance_check:
        print("Relevance check disabled (--no-relevance-check).", file=sys.stderr)

    # Download
    new_papers = deduplicate(results["papers_found"], output_dir)
    print(f"New (not yet on disk): {len(new_papers)}.", file=sys.stderr)

    for i, paper in enumerate(new_papers):
        if i >= args.max_papers * 2:
            break
        print(f"Downloading {i+1}/{len(new_papers)}: {paper.get('filename', '...')}", file=sys.stderr)
        results["downloads"].append(download_pdf(paper, output_dir))
        time.sleep(0.5)

    downloaded = sum(1 for d in results["downloads"] if d["status"] == "downloaded")
    existed = sum(1 for d in results["downloads"] if d["status"] == "exists")
    paywalled = sum(1 for d in results["downloads"] if d["status"] == "paywall")
    errs = sum(1 for d in results["downloads"] if d["status"] == "error")
    results["summary"] = {
        "total_found": len(results["papers_found"]) + len(results["filtered_out"]),
        "after_relevance_filter": len(results["papers_found"]),
        "filtered_out_count": len(results["filtered_out"]),
        "new_attempted": len(new_papers),
        "downloaded": downloaded,
        "already_existed": existed,
        "paywalled": paywalled,
        "errors": errs,
        "api_errors": len(results["errors"]),
        "relevance_check": (
            "disabled" if args.no_relevance_check
            else ("llm" if os.environ.get("OPENROUTER_API_KEY") else "rule_based")
        ),
    }

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
