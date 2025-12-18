# YouTube Playlist Downloader (OPUS)

## Introduction
This Python script allows you to download entire YouTube playlists and convert the audio to **OPUS format** at the highest possible quality.  
It reads playlist URLs from a `playlists.txt` file (one URL per line) and saves all downloaded tracks in organized folders.  

Key features:
- Downloads all tracks from multiple playlists.
- Converts audio to OPUS format using FFmpeg.
- Shows a summary of all downloaded tracks, including track number, title, and audio bitrate.
- Works fully in a Python virtual environment.

---

## Prerequisites
- Python 3.8 or higher installed.
- `pip` package manager.
- Git (optional, if cloning the repository).

---

## Setup

### 1. Create a virtual environment

#### On Windows:
```cmd
python -m venv myvenv
myvenv\Scripts\activate
```

#### On Linux / macOS:

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

---

### 2. Install dependencies

After activating the virtual environment, install all required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Usage

1. **Add playlist URLs** to `playlists.txt`, one URL per line:

```
https://www.youtube.com/playlist?list=PLxxxx...
https://www.youtube.com/playlist?list=PLyyyy...
```

2. **Run the downloader:**

```bash
python download_youtube_playlists.py
```

You will see a message:

```
===============================================
Please be patient, downloads are processing...
This may take a few minutes depending on playlist size.
===============================================
```

3. Wait for the download to finish. After all downloads, a summary of tracks with audio bitrate will be displayed.

---

## Directory and File Structure

After running the script, the downloaded playlists will be saved in the following structure:

```
Yt-playlist-downloader/
│
├── playlists.txt
├── download_youtube_playlists.py
├── requirements.txt
├── myvenv/                # Virtual environment
└── downloads/
    ├── Playlist Name 1/
    │   ├── Track 1.opus
    │   ├── Track 2.opus
    │   └── ...
    └── Playlist Name 2/
        ├── Track 1.opus
        ├── Track 2.opus
        └── ...
```

* Each playlist has its **own folder** inside the `downloads/` directory.
* Track filenames match their **YouTube titles**.
* Audio files are in **OPUS format**.

---

## Notes

* Ensure a stable internet connection for large playlists.
* The script runs entirely in the virtual environment; no system-wide FFmpeg installation is required.
* Bitrates may vary depending on the source audio quality on YouTube.

---


