---
aliases: []
categories:
- Recently Added
confidence: medium
created: '2026-07-14T21:03:14'
orphan: false
sources:
- file: /home/meyurin-2135327/wikis/pm-ru-wiki/raw_sources/Aljebreen et al - Predicting
    Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf
  hash: 9e49ad1daa1302f6a239e3b1d14985e53167040302d1f95eef9a74d034a426da
  ingested: '2026-07-14T21:03:14'
  size: 531581
  truncated: true
status: active
tags:
- pathway left shift
- care pathway
- patient deterioration
- ICU readmission
- surgical ward readmission
- machine learning
- deep learning
- event log
- EHR
- healthcare process management
title: Aljebreen Et Al   Predicting Pathway Left Shifts In Hospital Care Using Predictive
  Process Monitoring
type: technology
---

# Aljebreen Et Al   Predicting Pathway Left Shifts In Hospital Care Using Predictive Process Monitoring

Predicting Pathway Left Shifts in Hospital Care using 
Predictive Process Monitoring 
Abdulaziz Aljebreen1[0000-0002-4746-3446], Allan Pang1,2[0009-0008-2930-6077], Marc de 
Kamps1[0000-0001-7162-4425], and Owen Johnson1[0000-0003-3998-541X] 
1 School of Computer Science, University of Leeds, UK 
{ml17asa, ugm5a2p, m.dekamps, o.a.johnson}@leeds.ac.uk 
2 Royal Centre for Defence Medicine, UK 
Abstract. Hospitals worldwide are under pressure to use limited resources effi-
ciently while improving healthcare outcomes. Patients typically follow a linear 
care pathway (CP), moving from admission to surgery, acute care, recovery, and
discharge. A "left shift" occ urs when a patient returns from less acute to more 
acute care, indicating deterioration and potentially a premature transfer decision 
or poor care planning. Such left shifts disrupt hospital processes and negatively 
affect both patient outcomes a nd costs. Predicting left shifts can lead to better 
outcomes and allow clinicians to plan and adjust treatment. ^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:8-15]
This paper focuses on left shifts to the intensive care unit (ICU) or surgical 
ward (SW) as markers of patient deterioration. Our review of the literature found 
that previous studies on predicting ICU or SW left shifts have largely overlooked 
process aspects. Process Mining (PM) provides deeper contextual insights that 
can improve prediction accuracy, and predictive process monitoring (PPM) lev-
erages completed case traces to make predictions for ongoing cases. ^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:16-21]
We used the open -access MIMIC-IV dataset to evaluate the effectiveness of 
PPM in predicting ICU or SW left shifts, combining demographic, clinical, and 
process-related features. An event aggregation method was tested using machine 
learning (ML), deep learning (DL), and deep sequence (DS) models. Our results 
show that process -aware PPM significantly outperforms traditional prediction 
methods and demonstrates the potential to predict, plan for, or avoid left shifts, 
supporting smoother and more effective hospital care. ^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:22-28]
Keywords: Pathway Left Shift, Predictive Process Monitoring, Unplanned ICU 
Readmissions, Unplanned Surgery Ward Readmissions, Unplanned Reoperation, 
Clinical Pathway, Process Mining, Healthcare, Patient Flow Management, Event 
Log, EHR, MIMIC-IV, Machine Learning, Deep Learning, Deep Sequence. 
1 Introduction 
Healthcare is increasingly defined by the pressure to simultaneously achieve better pa-
tient outcomes and improved operational cost management. Hospitals are complex 
health systems responsible for delivering high -quality care and do this through stand-
ardised processes, procedures, technologies, and medications. Within a hospital, pa-
tients often follow a linear care pathway (CP) that is typically modelled as a process 
Pre-print copy of the paper accepted for presentation at the Process Mining Workshops (ICPM 2025 Int. Workshops), to appear in the Springer LNBIP series on Springer Link at https://link.springer.com/
2  A. Aljebreen, A. Pang, M. de Kamps and O. Johnson 
from left to right. For example, from planned or emergency admission, through surgery 
to acute care to recovery wards and through to dis -charge. We define a "left shift" as 
occurring when a patient returns back from less acute to more acute care, indicatin g a 
premature transfer, inadequate care planning or unresolved clinical issues [ 17]. Such 
left shifts to an intensive care unit (ICU) or surgical ward (SW) indicate a deteriorating 
patient, impacting patient outcomes and increasing healthcare costs [18]. ^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:34-46]
A large U.S. cohort study across 156 ICUs reported that approximately 2% of pa-
tients were readmitted to an ICU within 48 hours after transfer to a ward, and 3.7% 
within 120 hours [17]. Another study showed unplanned ICU readmissions are associ-
ated with a mortality rate of 21 – 40%, compared to just 3 – 8% in patients not readmit-
ted [18]. For unplanned re -operations (SW left shifts), one study found about 14% of 
patients with major head ^[Aljebreen et al - Predicting Pathway Left Shifts in Hospital Care using Predictive Process Monitoring.pdf:47-53]

## Key Data

- achieving AUROC = 0.80 and demonstrating improved performance over models using