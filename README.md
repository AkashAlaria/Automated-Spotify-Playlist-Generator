# Spotify Playlist Creator

## Description
This project is a Streamlit application that allows users to create a Spotify playlist based on an artist, genre, and the desired number of tracks. The application utilizes the Spotipy library to interact with the Spotify Web API.

## Requirements
- Python
- Streamlit
- Spotipy
- Spotify Web API credentials (Client ID and Client Secret)

## Installation
1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:

pip install streamlit spotipy

3. Obtain your Spotify Web API credentials (Client ID and Client Secret) from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

## Usage
1. Open the `main.py` file and replace the placeholders `client_id` and `client_secret` with your Spotify Web API credentials.
2. Run the application by executing the following command:

streamlit run main.py

3. The application will open in your default web browser.
4. Enter the desired artist name, genre, number of tracks, and playlist name in the respective fields.
5. Click the "Create Playlist" button to create a new Spotify playlist with the specified criteria.
6. Upon successful creation, a success message will be displayed, and the application will show a celebration animation.

## Features
- User-friendly Streamlit interface
- Create a new Spotify playlist based on specified criteria
- Specify the artist name, genre, number of tracks, and playlist name
- Success message and celebration animation upon successful playlist creation

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
