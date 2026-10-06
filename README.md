# Listening Analysis

A personal data analysis project exploring  listening habits using Python, Pandas, and data visualization libraries.

## Overview

This project analyzes streaming history to answer questions such as:

- Which artists are listened to most frequently?
- What songs accumulate the most listening time?
- How does listening activity change throughout the year?
- What hours of the day are most active?
- What percentage of tracks are skipped?

The analysis focuses on transforming raw listening history into meaningful insights and visualizations.

## Dataset

The project uses exported Spotify listening history data stored as CSV files.

Example fields:

- `ts` – timestamp
- `platform` – listening platform
- `ms_played` – milliseconds played
- `master_metadata_track_name` – track name
- `master_metadata_album_artist_name` – artist name
- `master_metadata_album_album_name` – album name
- `shuffle` – shuffle enabled
- `skipped` – track skipped
