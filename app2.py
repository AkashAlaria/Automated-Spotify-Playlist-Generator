import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://localhost:8080',
                                               scope='playlist-modify-private playlist-modify-public'))


def create_playlist(artist, genre, num, playlist_name):
    playlist = sp.user_playlist_create(sp.current_user()['id'], playlist_name, public=False)
    results = sp.search(q=f"artist:{artist} genre:{genre}", type='track', limit=num)
    track_uris = [track['uri'] for track in results['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_uris)
    return "Playlist created!"


def main():
    # Center aligning the logo
    col1, col2, col3 = st.columns([2, 3, 1])
    with col2:
        st.image("spotify.jpg", width=200)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Playlist Creator")

    artist = st.text_input("Enter artist name:")
    genre = st.text_input("Enter genre:")
    num = st.number_input("Enter number of tracks:", min_value=1, step=1)
    playlist_name = st.text_input("Enter playlist name:")

    if st.button("Create Playlist"):
        if artist and genre and num and playlist_name:
            message = create_playlist(artist, genre, num, playlist_name)
            success_message = st.success(message)
            success_message.text("Playlist created!")
            st.success("Playlist created successfully!")
            st.balloons()
        else:
            st.warning("Please fill in all fields.")


if __name__ == '__main__':
    main()
