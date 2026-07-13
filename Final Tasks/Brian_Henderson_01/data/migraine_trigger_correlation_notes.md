# Migraine trigger correlation notes - my analysis for Liu

Written 2026-10-19. My own read on the diary + Strava + OpenWeather data for the 30-day window ending 2026-10-21. This is the reasoning behind the count I want Liu to see. The assistant should be able to reproduce this from `migraine_diary_export_2026-10-21.csv` without needing this file - but this file is here as my author-side check.

## Analytic setup

- **Window:** 2026-09-22 through 2026-10-21 inclusive, 30 days.
- **Episode definition:** any day where `episode_present == 1` in the diary. No lookback smoothing, no partial-day fractional counts.
- **Trigger tag inclusion:** any tag appearing in `trigger_tag_primary`, `trigger_tag_secondary`, or `trigger_tag_tertiary` counts once per episode day.
- **Wearable corroboration threshold:**
  - Sleep score below 75 on the prior night
  - HRV below 35 ms on the prior night
  - Resting HR above 58 bpm on the prior night
  - Any two of the above = "wearable-corroborated sleep debt signal"
- **Weather corroboration threshold:**
  - Pressure delta of ≥ 6 hPa in the 24 hours before onset
  - Precipitation ≥ 1 mm on the same day (front indicator)
  - Either counts as "weather-driven day"

## The count

Iterating through the 30 days:

| Date | Episode? | Primary trigger | Wearable corroborated? | Weather corroborated? | Diary tag defensible? |
|---|---|---|---|---|---|
| 2026-09-22 | YES | weather_pressure_drop | yes (sleep 71) | yes (Δ-9 hPa, precip 4.2) | yes |
| 2026-09-25 | YES | skipped_meals | no (sleep 79) | no (Δ-1) | yes |
| 2026-09-28 | YES | poor_sleep | yes (sleep 68) | yes (Δ-6, precip 1.1) | yes |
| 2026-09-30 | YES | weather_pressure_drop | no (sleep 74 borderline) | yes (Δ-10, precip 3.5) | yes |
| 2026-10-04 | YES | fluorescent_light_office | no (sleep 77) | no (Δ-5) | yes |
| 2026-10-07 | YES | poor_sleep | yes (sleep 69) | yes (Δ-6) | yes |
| 2026-10-12 | YES | weather_pressure_drop | yes (sleep 66) | yes (Δ-15, precip 6.8) | yes (two Nurtec doses) |
| 2026-10-15 | YES | poor_sleep | no (sleep 72 borderline) | no (Δ-2) | yes |
| 2026-10-19 | YES | skipped_meals | no (sleep 76) | no (Δ-3) | yes |

**Total episode count: 9 episodes in 30 days.**

## Trigger frequency ranking

Counting each trigger tag (primary + secondary + tertiary) across the 9 episode days:

| Trigger tag | Days appearing as primary | Days appearing as secondary | Days appearing as tertiary | Total | Avg severity on days present |
|---|---|---|---|---|---|
| weather_pressure_drop | 3 (9/22, 9/30, 10/12) | 0 | 0 | 3 | 7.0 |
| poor_sleep | 3 (9/28, 10/7, 10/15) | 0 | 1 (10/12) | 4 | 7.25 |
| skipped_meals | 2 (9/25, 10/19) | 1 (10/7) | 0 | 3 | 6.0 |
| stress_manuscript | 0 | 2 (9/28, 10/12) | 0 | 2 | 7.5 |
| fluorescent_light_office | 1 (10/4) | 1 (9/25) | 0 | 2 | 5.5 |

**Ranked top three by total appearance:**
1. **poor_sleep** - 4 total appearances, avg severity 7.25
2. **weather_pressure_drop** - 3 total appearances, avg severity 7.0
3. **skipped_meals** - 3 total appearances, avg severity 6.0

Tiebreaker between weather_pressure_drop and skipped_meals: weather_pressure_drop has a higher avg severity (7.0 vs 6.0), so it ranks second and skipped_meals ranks third.

## What this changes vs the stored-memory summary

- Stored-memory summary said "6 to 8 per month" - data says **9** in this window.
- Stored-memory framed the trigger picture around weather. Data says **sleep debt and weather are roughly tied**, and skipped meals is the third rail. My office fluorescent-light theory is real but statistically minor in this window.
- **The count I hand Liu is 9, with the top three triggers being poor sleep, weather pressure drop, and skipped meals in that order.**

## Confidence and caveats

- Two episode days (10/15, 10/19) had no wearable or weather corroboration and rest on the diary tag alone. They stay in the count because the diary is contemporaneous and I do not drop episodes without reason. Liu should see them called out separately as "diary-tag-only" if he wants to interrogate them.
- The 10/12 episode is my highest severity (8/10, two Nurtec doses). It coincided with the day after the Henderson family reunion in Stamford - sleep debt, weather drop, and manuscript stress all present. Multi-trigger day. Not a typical episode.
- The stress_manuscript tag is undercounted here because I do not always tag it. It is present on days I know I was stressed about the NEJM revision cycle. This is subjective and I do not want Liu to overweight it.

## Guard

This file stays on my personal filesystem. Nothing here reaches:
- The family chat
- The Windbridge Outlook thread with Foster
- The Windbridge first-gen STEM ERG channel
- Teams / Slack / Confluence
- Boston IVF nurse coordinator (different lane - Cheng and Karen Miller do not need this either)

Only the Dr. Liu draft note derived from this file, held at draft in Box, ever gets shared - and only after I review it in person.
