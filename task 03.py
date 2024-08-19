import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Replace 'your_access_token' with your actual Genius API access token
GENIUS_API_TOKEN = 'your_access_token'

# Initialize the Genius API
genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

def get_lyrics():
    artist = artist_entry.get().strip()
    song = song_entry.get().strip()
    if not artist or not song:
        messagebox.showerror("Error", "Please enter both artist and song name!")
        return

    try:
        song_info = genius.search_song(song, artist)
        if song_info:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song_info.lyrics)
        else:
            messagebox.showerror("Error", "Lyrics not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Lyrics Finder")

# Create and place the labels, entries, and button
tk.Label(root, text="Artist:").grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=40)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Song:").grid(row=1, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, width=40)
song_entry.grid(row=1, column=1, padx=10, pady=10)

fetch_button = tk.Button(root, text="Get Lyrics", command=get_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Text widget to display the lyrics
lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()