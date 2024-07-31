import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def music_recommendation():

    # Retrieve credentials from environment variables
    CLIENT_ID = st.secrets["CLIENT_ID"]
    CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

    # Initialize the Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_song_album_cover_url(song_name, artist_name):
        search_query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=search_query, type="track")

        if results and results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            album_cover_url = track["album"]["images"][0]["url"]
            return album_cover_url
        else:
            return "https://i.postimg.cc/0QNxYz4V/social.png"

    def recommend(song):
        index = music[music['song'] == song].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_music_names = []
        recommended_music_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            artist = music.iloc[i[0]].artist
            recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
            recommended_music_names.append(music.iloc[i[0]].song)

        return recommended_music_names,recommended_music_posters

    st.title('Music Recommendation')
    music = pickle.load(open('models/df_music.pkl','rb'))
    similarity = pickle.load(open('models/similarity_music.pkl','rb'))

    music_list = music['song'].values
    selected_movie = st.selectbox("Select a song from the dropdown", music_list,index=None)

    if st.button('Recommend'):
        if selected_movie:
            recommended_music_names,recommended_music_posters = recommend(selected_movie)
            col1, col2, col3, col4, col5= st.columns(5)
            with col1:
                st.text(recommended_music_names[0])
                st.image(recommended_music_posters[0])
            with col2:
                st.text(recommended_music_names[1])
                st.image(recommended_music_posters[1])
    
            with col3:
                st.text(recommended_music_names[2])
                st.image(recommended_music_posters[2])
            with col4:
                st.text(recommended_music_names[3])
                st.image(recommended_music_posters[3])
            with col5:
                st.text(recommended_music_names[4])
                st.image(recommended_music_posters[4])
        else:
            st.warning('Please select a song before clicking the recommend button.')

music_recommendation()
