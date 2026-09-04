# IP-WQ-126 — Other inbound pipes

**Status:** OPEN
**Date:** 2026-09-04 10:58 EDT
**Priority:** medium
**Parent:** IP-WQ-095 / 096 / 080

## Allowed sources

| kind | how it arrives |
|------|----------------|
| youtube-short | URL in message |
| youtube-long | watch URL; stills via ffmpeg after cookies (081) |
| still | one dropped image |
| ig-export / fb-export / tt-export | official takeout or user dump folder. **No live scrapers.** |

## Databases looked at (research only, 2026-09-04)

YouTube Data API v3 (no Shorts type). yt-research 0.2.0. Social Fetch / Apify as third-party envelopes. Academic Shorts corpora. Synthetic "trends" tables are not mouths.

## Done when

Boot accepts a still or export folder the same way it accepts a Short URL. No Apify key in the skill.
