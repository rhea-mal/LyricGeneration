import streamlit as st
from datetime import time
from main import *
from streamlit_extras.let_it_rain import rain

ARTISTS = ['Phoebe Bridgers', 'Eminem', 'Coldplay', 'Julien Baker', 'Drake', 'Lucy Dacus', 'Justin Bieber', 'John Mayer', 'Beyonce', 'Issac Gracie', 'Billie Marten', 'Novo Amor', 'Adam Melchor', 'Hozier', 'Khalid', 'Iron  Wine', 'Ben Howard', 'Katy Perry', 'Cardi B', 'Rihanna', 'Ariana Grande', 'James Bay', 'Dua Lipa', 'Nicki Minaj', 'BTS', 'Ed Sheeran', 'Angelo De Augustine', 'Selena Gomez', 'Maroon 5', 'Taylor Swift', 'Post Malone', 'Charlie Puth', 'Billie Eilish', 'Lady Gaga']
GENRES = ['indie-pop', 'anime', 'folk', 'brazil', 'chill', 'guitar', 'acoustic', 'metalcore', 'groove', 'ambient', 'afrobeat', 'gospel', 'garage', 'singer-songwriter', 'j-rock', 'drum-and-bass', 'black-metal', 'iranian', 'blues', 'study', 'british', 'dub', 'goth', 'idm', 'detroit-techno', 'deep-house', 'dance', 'edm', 'grindcore', 'electronic', 'dancehall', 'chicago-house', 'electro', 'pop', 'opera', 'j-dance', 'alt-rock', 'club', 'rockabilly', 'children', 'hardstyle', 'death-metal', 'disco', 'breakbeat', 'country', 'swedish', 'progressive-house', 'show-tunes', 'emo', 'party', 'grunge', 'hip-hop', 'soul', 'piano', 'punk-rock', 'j-pop', 'comedy', 'industrial', 'cantopop', 'kids', 'indian', 'alternative', 'k-pop', 'turkish', 'bluegrass', 'minimal-techno', 'trance', 'dubstep', 'reggae', 'rock-n-roll', 'power-pop', 'french', 'honky-tonk', 'sad', 'house', 'hardcore', 'ska', 'latin', 'happy', 'rock', 'punk', 'pop-film', 'spanish', 'techno', 'new-age', 'synth-pop', 'german', 'funk', 'trip-hop', 'sleep', 'latino', 'classical', 'psych-rock', 'r-n-b', 'metal', 'hard-rock', 'disney', 'world-music', 'mpb', 'malay', 'jazz', 'salsa', 'j-idol', 'mandopop']

def main():
    st.title("Lyricade :lemon:")

    st.subheader("Drop a Beat!")
    st.caption("""
   Our NLP model analyzes any piece of music, and based on its overall tone and energy, can generate lyrics! Upload your instrumental, pick a genre and artist, and watch the magic happen! By Klara, Arnav, and Rhea :)
   """)


    uploaded_file = st.file_uploader("mp3 | wav", type=['wav', 'mp3'])
    st.divider()
    if uploaded_file:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        st.divider()
        st.markdown(f'<span style="color: #d67ea6; font-weight: bold;">Basics & Essentials :sparkles:</span>', unsafe_allow_html=True)
        tempo = st.slider('Tempo', 50, 200, 1)
        duration_ms = (st.slider(
            "Duration:", min_value= time(0,30), max_value= time(5,00),
            value=(time(0, 0), time(5, 00))))
        loudness = st.slider('Loudness', -35.0, -0.1, 0.1)     

        st.markdown(f'<span style="color: #a6e892; font-weight: bold;">Sound & Texture :trumpet:</span>', unsafe_allow_html=True)

        instrumentalness = st.slider('Instrumentalness', 0, 100, 1) / 100
        acousticness = st.slider('Acousticness', 0, 100, 1) / 100
        liveness = st.slider('Liveness', 0, 100, 1) / 100

        st.markdown(f'<span style="color: #d3b0f7; font-weight: bold;">Vibes & Mood :fire:</span>', unsafe_allow_html=True)
        valence = st.slider('Valence', 0, 100, 1) / 100
        energy = st.slider('Energy', 0, 100, 1) / 100
        popularity = st.slider('Popularity', 0, 100, 1) / 100
        
        st.markdown(f'<span style="color: #f7925c; font-weight: bold;">Customization :star:</span>', unsafe_allow_html=True)


        artist = st.selectbox(
    'Select an artist',
    ARTISTS)
        
        genre = st.selectbox(
    'Select a desired genre',
    GENRES)

        explicit = st.toggle('Explicit')

        if explicit:
            explicit = 2.826916
        else:
            explicit = 	-0.353742	

        max_time = duration_ms[1]
        max_hours = max_time.hour
        max_minutes = max_time.minute

        # convert slider to ms
        max_duration_ms = ((max_hours * 60 * 60 * 1000) + (max_minutes * 60 * 1000)) / 60

        generate = st.button(":microphone:", type="primary", use_container_width=True)

        if generate:
            lyrics = start_generation(artist, genre, explicit, uploaded_file)
            st.divider()
            st.subheader(lyrics)

            rain(
                emoji="🍋",
                font_size=54,
                falling_speed=10,
                animation_length="infinite",
            )


if __name__ == "__main__":
   main()

