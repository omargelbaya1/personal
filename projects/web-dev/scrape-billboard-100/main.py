import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header={"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}




url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)    

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


# print(song_names)




year = date.split("-")[0]



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               client_id="",
                                               client_secret="",
                                               redirect_uri="https://example.com",
                                               username="habashiba",
                                               cache_path=".cache-habashiba",
                                               show_dialog=True
                                               ))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])


user_id=sp.current_user()["id"]




list_of_urls=[]
for i in song_names:
    try:
        track=sp.search(q=f"track: {i}  year:{year}" ,limit=10, offset=0, type='track', market=None)
        list_of_urls.append(track["tracks"]["items"][0]["artists"][0]["external_urls"]["spotify"])
    except:
        pass

playlist=sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)

print(playlist)


sp.playlist_add_items(playlist_id=playlist["id"], items=list_of_urls)