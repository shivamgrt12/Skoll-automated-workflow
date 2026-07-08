# TAVR Study Protocol of Record, Summary

Reference document for the fellowship wiki. Reflects the currently approved protocol as of amendment 4.

## Analysis Pipeline

Primary analysis pipeline is a Cox proportional hazards model with site as a random effect, adjusted for STS-PROM score tercile, age, sex, and baseline eGFR. Bootstrap resampling with 1000 iterations for confidence intervals.

Secondary analyses:
- Landmark analysis at 30 days for 1-year MACE
- Competing risks analysis for cardiovascular mortality vs non-cardiovascular mortality
- Subgroup analysis by STS-PROM tercile

## Biostatistics Repository

Analysis code is maintained in the shared biostatistics repository (`ccp-tavr-analysis`). The branch of record is `main`.

Deviations from protocol pipeline require amendment approval before analysis outputs can enter the manuscript.

## Software Environment

- R version 4.3.2
- survival package 3.5-7
- lme4 package 1.1-35
- boot package 1.3-28

## Notes

The `main` branch was last audited by the biostatistics core on 2026-08-01. Any subsequent commits should be reviewed against the protocol before figures are pulled for the manuscript.
