

# Capstone Project 1 - Jovita Gandhi
import json
import pandas as pd

with open('Data/spotify_million_playlist_dataset/Main_data/mpd.slice.0-999.json') as f:
    data = json.load(f)

# print(data)

# Create an empty list to store the flattened playlists
flattened_playlists = []

# Iterate over each playlist
for playlist in data['playlists']:

    # Iterate over each track in the playlist
    for track in playlist['tracks']:

        # Create a new dictionary to store the flattened data
        flattened_data = {}

        # Add the playlist-level data to the flattened dictionary
        flattened_data['pid'] = playlist['pid']
        flattened_data['name'] = playlist['name']
        flattened_data['collaborative'] = playlist['collaborative']
        flattened_data['modified_at'] = playlist['modified_at']
        flattened_data['num_tracks'] = playlist['num_tracks']
        flattened_data['num_albums'] = playlist['num_albums']
        flattened_data['num_followers'] = playlist['num_followers']

        # Add the track-level data to the flattened dictionary
        flattened_data['pos'] = track['pos']
        flattened_data['artist_name'] = track['artist_name']
        flattened_data['track_uri'] = track['track_uri']
        flattened_data['artist_uri'] = track['artist_uri']
        flattened_data['track_name'] = track['track_name']
        flattened_data['album_uri'] = track['album_uri']
        flattened_data['duration_ms'] = track['duration_ms']
        flattened_data['album_name'] = track['album_name']

        # Add the flattened data to the list
        flattened_playlists.append(flattened_data)

# Create a DataFrame from the flattened list of playlists
df = pd.DataFrame(flattened_playlists)
