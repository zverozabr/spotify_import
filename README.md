example inside in run.py
---

## Importing Liked Songs from Spotify Using Python

### Step 1: Install the Spotipy Library

First, install the `spotipy` library. You can do this using pip:

```bash
pip install spotipy
```

### Step 2: Set Up Spotify API Credentials

You need to register your application on the Spotify Developer Dashboard to get the necessary credentials:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Create a new app and note down the Client ID and Client Secret.

### Step 3: Authorize and Authenticate

Use the Spotipy library to authorize your application. Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_REDIRECT_URI` with your own details.

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="YOUR_REDIRECT_URI",
                                               scope="user-library-read"))
```

Make sure to set the `scope` to `"user-library-read"` to access liked songs.

### Step 4: Fetch Liked Songs

Now, you can fetch the liked songs:

```python
def get_liked_songs(sp):
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx + 1}. {track['artists'][0]['name']} – {track['name']}")

# Call the function
get_liked_songs(sp)
```

This function will print a list of liked songs from your Spotify account.

### Notes

- Ensure your Spotify app has the necessary permissions set in the developer dashboard.
- The redirect URI in the Spotify application settings and your code should match.
- If you encounter a token error, check your credentials and the set scope.

---

This guide assumes basic familiarity with Python and the use of API keys. Remember to handle your credentials securely and never expose them in your code, especially in public repositories.