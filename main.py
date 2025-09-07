import os
import csv
import requests
import tkinter as tk
from tkinter import messagebox, ttk
import threading

API_KEY = "your-API-key"
BASE_DIR = r"C:\Omkar\Youtube videos\Channel Data CSV"
CSV_FILE = os.path.join(BASE_DIR, "channel_videos.csv")

# ==============================
# YouTube Data Functions
# ==============================
def resolve_channel_id(channel_url):
    if "channel/" in channel_url:
        return channel_url.split("channel/")[1].split("/")[0]
    elif "user/" in channel_url:
        username = channel_url.split("user/")[1].split("/")[0]
        url = f"https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={username}&key={API_KEY}"
        res = requests.get(url).json()
        return res["items"][0]["id"] if "items" in res else None
    elif "@" in channel_url:
        handle = channel_url.split("@")[1].split("?")[0].split("/")[0]
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={handle}&key={API_KEY}"
        res = requests.get(url).json()
        return res["items"][0]["snippet"]["channelId"] if "items" in res else None
    return None

def get_uploads_playlist_id(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={API_KEY}"
    res = requests.get(url).json()
    if "items" in res and res["items"]:
        return res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    return None

def get_all_videos(channel_url, progress_callback=None):
    channel_id = resolve_channel_id(channel_url)
    if not channel_id:
        return None

    uploads_playlist_id = get_uploads_playlist_id(channel_id)
    if not uploads_playlist_id:
        return None

    videos = []
    next_page_token = None
    fetched_count = 0

    while True:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&maxResults=50&key={API_KEY}"
        if next_page_token:
            url += f"&pageToken={next_page_token}"

        res = requests.get(url).json()
        if "items" not in res:
            break

        for item in res["items"]:
            snippet = item["snippet"]
            videos.append({
                "title": snippet["title"],
                "description": snippet.get("description", ""),
                "published_at": snippet["publishedAt"],
                "video_url": f"https://www.youtube.com/watch?v={snippet['resourceId']['videoId']}"
            })
            fetched_count += 1
            if progress_callback:
                progress_callback(fetched_count)

        next_page_token = res.get("nextPageToken")
        if not next_page_token:
            break

    return videos

# ==============================
# CSV Function
# ==============================
def save_to_csv(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "description", "published_at", "video_url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    messagebox.showinfo("Success", f"Video data saved to:\n{file_path}")

# ==============================
# GUI Functions
# ==============================
def start_scraping():
    channel_url = entry.get().strip()
    if not channel_url:
        messagebox.showwarning("Input Error", "Please enter a channel URL.")
        return

    button.config(state="disabled")
    progress_bar["value"] = 0
    progress_label.config(text="Fetching videos...")

    # Run scraping in a separate thread
    threading.Thread(target=fetch_videos_thread, args=(channel_url,)).start()

def fetch_videos_thread(channel_url):
    videos = get_all_videos(channel_url, progress_callback=update_progress)
    if videos:
        save_to_csv(videos, CSV_FILE)
    else:
        messagebox.showerror("Error", "Failed to fetch videos.")
    button.config(state="normal")
    progress_label.config(text="Done!")

def update_progress(count):
    # This runs in the thread, update GUI using `after`
    def _update():
        progress_bar["value"] = count % 100  # rough progress indicator
        progress_label.config(text=f"Videos fetched: {count}")
    root.after(0, _update)

# ==============================
# GUI Setup
# ==============================
root = tk.Tk()
root.title("YouTube Channel Video Scraper")
root.geometry("550x200")

tk.Label(root, text="Enter YouTube Channel URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

button = tk.Button(root, text="Fetch & Save Videos", command=start_scraping, bg="red", fg="white")
button.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)
progress_label = tk.Label(root, text="", font=("Arial", 10))
progress_label.pack()

root.mainloop()
