import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
import os

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = "http://localhost:8888/callback"
scope = 'user-library-read'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    )
)

# Получение списка любимых треков
track_data = []
offset = 0
limit = 50  # Максимальное значение

while True:
    tracks = sp.current_user_saved_tracks(limit=limit, offset=offset)
    for item in tracks['items']:
        track = item['track']
        track_data.append([track['name'], track['artists'][0]['name'], track['album']['name']])

    if len(tracks['items']) < limit:
        break
    offset += limit

# Экспорт в CSV
with open('spotify_favorites.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Track Name', 'Artist', 'Album'])
    writer.writerows(track_data)
