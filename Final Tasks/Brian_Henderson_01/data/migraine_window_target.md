# Migraine window target - for Dr. Liu 2026-10-22 2:30 PM Deerfield Wellness

Written 2026-10-19 evening. I need to walk in Thursday with the count the data will defend, not the number I have been quoting to Sarah and to Foster. The CGRP preventive conversation with Liu is going to hinge on the count.

## The window

**Rolling 30 days ending 2026-10-21** (the day before the visit).
- Start: 2026-09-22 (Tuesday)
- End: 2026-10-21 (Wednesday)
- Inclusive on both ends.

## Data sources to reconcile

1. **Airtable migraine diary** (my daily log): episode present flag, onset time, duration, severity 1-10, Nurtec doses, aura, trigger tags primary/secondary/tertiary, notes. Cross-verify against `migraine_diary_export_2026-10-21.csv`.
2. **Strava wearable log**: sleep score, sleep hours, HRV ms, resting HR, ran-that-day. My personal baseline: sleep score 80+, HRV 40+, RHR 54-56. Anything meaningfully below → sleep debt / high stress signal.
3. **OpenWeather** for Cambridge, MA (42.3736, -71.1097): daily pressure hPa, 24-hour pressure delta, temp, precipitation. Baseline pressure ~1017 hPa. Deltas ≥ 6 hPa in 24 hours are the pressure-drop days.

## The count I will hand him

Episode count over the window: **[reconcile from the three sources above]**

- Reasoning: an episode day is any day where `episode_present == 1` in the diary. Cross-check that the same day shows either (a) a Strava sleep score below 75 the prior night, or (b) an OpenWeather pressure delta ≥ 6 hPa in 24 hours, or (c) a diary tag matching one of my known triggers (skipped meals, fluorescent lights, poor sleep, stress-manuscript). If two of the three signals agree, the day is a defensible episode.

- What I have been telling people: **6 to 8 per month**. This is the stored-memory version. It is stale from spring 2026 and Liu should not see it as the current picture.

- What the diary + wearable + weather actually show for this window: **[fill from the reconciled count]**.

## Top three correlated triggers ranked by frequency in the window

Rank by count of episode days where each trigger tag appears as `trigger_tag_primary` OR `trigger_tag_secondary`, breaking ties by average severity.

1. [ ] _(weather_pressure_drop is my strong prior, based on the Sept 22, Sept 30, Oct 12 episodes)_
2. [ ] _(poor_sleep and skipped_meals are the other two I expect)_
3. [ ] _(fluorescent_light_office and stress_manuscript compete for third)_

## Questions I want to hand Liu

- I have been on Nurtec 75 mg PRN for two years. Response time trend is stable (~40-55 minutes to relief). Is the CGRP preventive (Aimovig 70 mg) the right next step given the count?
- If we do add Aimovig, what is the taper or overlap with Nurtec PRN? Can I keep Nurtec for breakthrough?
- What is the sensitivity of the CGRP preventive class to weather-pressure trigger patterns? My primary trigger looks weather-driven.
- Given the IVF stim cycle is starting in November and Sarah is the patient, are any of the CGRP preventives contraindicated or relatively contraindicated in a partner-of-patient context, or is that not a consideration?
- Are there interactions to watch with Lexapro 10 mg daily? He should have this in the chart from Cheng but confirm.
- Do I need a headache diary format for a preventive trial, or is the Airtable + Strava + OpenWeather reconciliation I already do sufficient?

## What I refuse to walk in with

- Two different episode numbers in my own file
- A memory summary the data will not defend
- A trigger list the diary tag does not support
- A stress narrative that skips the manuscript deadline and the finals block context (both feed the count)
- A pretense that I have controlled for the office fluorescent-light exposure when I clearly have not

## Guard on this note

This note stays personal. Nothing here reaches the Windbridge Outlook thread with Foster, the Teams migraine wellness channel, the Slack ERG channel, or the Stamford family chat. Patricia does not need to hear the specifics on the standing Sunday call. Sarah has read this draft. Dr. Cheng and Dr. Karen Miller do not need this specific note - their notes are separate. Only Liu.
