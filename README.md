# YouTube Playlist Downloader (OPUS)

## Introduction
This project is a Python-based YouTube playlist downloader that extracts **high-quality audio** and converts it into **OPUS format**.  
It supports downloading **multiple playlists**, organizes tracks neatly into folders, and prints a clean **download summary** including audio bitrates.

The script runs fully inside a **Python virtual environment**, keeping your system clean.

---

## Features
- Download full YouTube playlists
- Best available audio quality
- Automatic OPUS conversion
- Clean download summary (track number, title, bitrate)
- Works inside a Python virtual environment (venv)

---

## Prerequisites
- Python **3.8+**
- `pip`
- Git

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Yt-playlist-downloader.git
cd Yt-playlist-downloader
````

---

## Environment Setup

### 2. Create a virtual environment

#### Windows

```cmd
python -m venv myvenv
myvenv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

---

### 3. Install dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

---

## Usage

### 4. Add playlist URLs

Open `playlists.txt` and add **one playlist URL per line**:

```
https://www.youtube.com/playlist?list=PLxxxx...
https://www.youtube.com/playlist?list=PLyyyy...
```

---

### 5. Run the downloader

```bash
python download_youtube_playlists.py
```

After starting, you will see:

```
===============================================
Please be patient, downloads are processing...
This may take a few minutes depending on playlist size.
===============================================
```

Once all downloads are complete, a **download summary** is printed.

<img width="1078" height="507" alt="Download Summary Example" src="https://github.com/user-attachments/assets/c58c7e81-02c7-4eaa-bed5-78ae07d043f0" />

---

## Output Directory Structure

After execution, files are organized as follows:

```
Yt-playlist-downloader/
│
├── playlists.txt
├── download_youtube_playlists.py
├── requirements.txt
├── myvenv/                  # Virtual environment
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

### Notes on Output

* Each playlist gets its **own folder**
* Track names match their **YouTube titles**
* All audio files are saved in **OPUS format**

---

## Notes & Tips

* Large playlists may take time — please be patient.
* Audio bitrate depends on the original YouTube source.
* No system-wide FFmpeg installation is required.
* Keep the virtual environment activated while running the script.

