import yt_dlp
import os

# -----------------------------
# Friendly start message
# -----------------------------
print("\n===============================================")
print("Please be patient, downloads are processing...")
print("This may take a few minutes depending on playlist size.")
print("===============================================\n")

# -----------------------------
# Configuration
# -----------------------------
PLAYLIST_FILE = "playlists.txt"
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(PLAYLIST_FILE):
    print(f"Error: {PLAYLIST_FILE} not found!")
    exit(1)

with open(PLAYLIST_FILE, "r") as f:
    playlist_urls = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

if not playlist_urls:
    print("No playlist URLs found in the file!")
    exit(1)

all_tracks = []

# -----------------------------
# Progress hook
# -----------------------------
def my_hook(d):
    if d['status'] == 'finished':
        info = d['info_dict']
        track_num = info.get('playlist_index', '?')
        title = info.get('title', 'Unknown Title')
        playlist = info.get('playlist', 'Unknown Playlist')
        abr = info.get('abr', 'unknown')

        all_tracks.append({
            "playlist": playlist,
            "track_num": track_num,
            "title": title,
            "bitrate": abr
        })

# -----------------------------
# yt-dlp options
# -----------------------------
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(playlist_title)s', '%(title)s.%(ext)s'),
    'ignoreerrors': True,
    'noplaylist': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
        'preferredquality': '0',
    }],
    'progress_hooks': [my_hook],
    'quiet': True,
    'no_warnings': True,
}

# -----------------------------
# Download playlists
# -----------------------------
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in playlist_urls:
        try:
            info = ydl.extract_info(url, download=False)
            playlist_title = info.get('title', 'Unknown Playlist')
            num_tracks = info.get('playlist_count', '?')

            print("\n" + "="*80)
            print(f"Downloading playlist: {playlist_title} | Total tracks: {num_tracks}")
            print("="*80)

            ydl.download([url])

        except Exception as e:
            print(f"Error downloading playlist {url}: {e}")

# -----------------------------
# Print final summary
# -----------------------------
print("\n" + "="*80)
print("Download Summary:")
print("="*80)
for track in all_tracks:
    print(f"[{track['playlist']}] Track {track['track_num']:>2}: {track['title']:<50} | Audio bitrate: {track['bitrate']} kbps")

print("\nAll playlists processed!")
