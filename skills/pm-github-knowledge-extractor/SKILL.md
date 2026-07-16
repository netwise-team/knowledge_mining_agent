---
name: pm-github-knowledge-extractor
type: instruction
version: 1.0.0
description: Automatically extracts and ingests GitHub repository references from Process Mining articles into pm-wiki, creating dedicated pages with structured implementation knowledge and bidirectional cross-links.
---

# pm-github-knowledge-extractor

## Trigger

When analyzing any Process Mining article, paper, or document — regardless of how it was discovered (web_search result, synthadoc_ingest candidate, direct URL fetch, or user-provided link) — automatically extract all GitHub repository references and ingest their implementation knowledge into the wiki.

## Standing Behavioral Instruction

This skill permanently encodes the following research workflow into Ouroboros behavior. Every time a Process Mining article or document is analyzed, the following steps MUST be performed in addition to the primary analysis task.

---

### Step 1 — Scan for GitHub Repository URLs

After reading or ingesting any PM article, scan the full text for repository references in these locations:
- **Footnotes and endnotes** — any `github.com/*` link in a note marker
- **References / Bibliography section** — look for `github.com/`, `arxiv.org` links with "code" in title or body, or DOI entries that link to software
- **Inline citations** — phrases like "code available at", "implementation at", "source code at", "released at", "our implementation", "open-source", "we provide code"
- **Abstract and contribution bullets** — authors often advertise code availability here

Patterns to match:
- `github.com/<owner>/<repo>` (direct link, any path depth)
- `arxiv.org/abs/XXXX` with accompanying "code" mention nearby
- Bare owner/repo references like "available at github: owner/repo"

For each unique repository found, proceed to Step 2.

---

### Step 2 — Fetch README and Key Source Files

For each discovered GitHub repository `github.com/<owner>/<repo>`:

1. **Primary fetch** via `run_command`:
   ```
   run_command(["curl", "-sL", "--max-time", "30",
       "https://raw.githubusercontent.com/<owner>/<repo>/main/README.md"])
   ```
2. **Fallback** (if primary returns 404 or empty):
   ```
   run_command(["curl", "-sL", "--max-time", "30",
       "https://raw.githubusercontent.com/<owner>/<repo>/master/README.md"])
   ```
3. If README references specific source files (e.g. `src/model.py`, `algorithms/discovery.py`) and those files are small (<500 lines), fetch them too using the same curl pattern with the appropriate path.
4. If both curl attempts fail, use `web_search` for the repository page as a last resort.

---

### Step 3 — Extract Structured Knowledge

From the fetched README and source files, extract:

| Field | What to look for |
|---|---|
| **What it does** | One-paragraph functional description |
| **Architecture** | Main components, modules, class hierarchy if mentioned |
| **Key algorithms** | Named algorithms (e.g. Alpha Miner, Inductive Miner, GRU-based predictor) |
| **Authors** | From README, paper citation, or `setup.py`/`pyproject.toml` |
| **License** | LICENSE file reference or badge in README |
| **Dependencies** | `requirements.txt`, `setup.py` install_requires, or README "Installation" section |
| **Supported datasets** | Benchmark datasets mentioned (BPI Challenge years, Sepsis, RTFM, etc.) |
| **Relation to article** | How the repo implements or reproduces the article's claims; which experiments it enables |

---

### Step 4 — Ingest into pm-wiki

#### Primary method — `synthadoc_ingest`

Call:
```
mcp_synthadoc__synthadoc_ingest(source="https://github.com/<owner>/<repo>")
```

After calling, check job status with `mcp_synthadoc__synthadoc_jobs(status="all")` and wait for completion. If a candidate page appears, promote it via the `synthadoc` CLI binary (which IS available in the environment as a shell command — this is NOT an MCP tool call):
```
run_command(["synthadoc", "candidates", "promote", "<repo-slug>", "-w", "pm-wiki"])
```
Note: `synthadoc candidates` subcommands are `list`, `promote`, and `discard` — there is no `show` subcommand. To read a candidate file before promoting, use `read_file` directly on the candidate path at `<wiki-root>/wiki/candidates/<slug>`.

#### Fallback method — `synthadoc_write_page`

If `synthadoc_ingest` fails, returns an error, or produces an empty/malformed candidate, manually construct and write a wiki page using:
```
mcp_synthadoc__synthadoc_write_page(
    slug="<repo-name>",
    title="<RepoName> — GitHub Implementation",
    content=<structured markdown content>
)
```

The page content MUST include:
- A `resource:` frontmatter field: `https://github.com/<owner>/<repo>`
- Sections: Overview, Architecture, Key Algorithms, Installation, Supported Datasets, Related Articles, License
- A "Related Articles" section listing the parent article wiki slug(s)

After writing, transition to active:
```
mcp_synthadoc__synthadoc_lifecycle(slug=<slug>, to_state="active",
    reason="manually extracted from GitHub")
```

---

### Step 5 — Cross-Link Bidirectionally

After the repository wiki page exists (either promoted or written):

1. **Repository page → Article page:** The page written in Step 4 must contain a "Related Articles" section with wiki links to the parent article slug.

2. **Article page → Repository page:** Read the existing article page with `mcp_synthadoc__synthadoc_read_page(slug=<article-slug>)`, find the References or Implementation section, and add a cross-reference link to the repository slug. Update with `mcp_synthadoc__synthadoc_write_page`.

Both links must be present before the step is considered complete.

---

### Execution Order and Integration

This workflow runs **after** the primary article analysis. It must not block or delay the main answer to the user. The correct order is:

1. Answer the user's question from the article content.
2. Then execute Steps 1–5 for any repositories found.
3. Report a compact summary: "Found N GitHub repos in citations; ingested: [list of slugs]."

If no GitHub repositories are found in the article, this workflow completes immediately with no action.

---

### Error Handling

- If `synthadoc_ingest` returns an error for a GitHub URL, wait 10 seconds and retry once; if it fails again, fall back to manual `synthadoc_write_page`.
- If `curl` times out fetching a README, try the alternate branch (`master` vs `main`) once; if both fail, write a stub page with the repository URL and note "README fetch failed — manual review needed."
- If the article page no longer exists in the wiki (e.g. was archived), still create the repository page but skip the bidirectional article link and log a warning.
- Never fail silently: always report which repos were found, which were successfully ingested, and which failed.
- Before ingesting, check `mcp_synthadoc__synthadoc_search` for the repository slug to avoid duplicate pages.

---

### Scope

This workflow applies to:
- All Process Mining papers discovered via `web_search`
- All articles ingested via `mcp_synthadoc__synthadoc_ingest`
- All PM documents provided directly by the user (PDF, URL, or pasted text)
- All articles already in pm-wiki that are revisited in conversation

This workflow does NOT apply to:
- Non-PM articles (software engineering, general ML without PM content)
- GitHub repositories that are already present in pm-wiki
- Private or 404 repositories (skip gracefully after one failed fetch attempt)
