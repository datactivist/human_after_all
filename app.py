import streamlit as st 
from streamlit_player import st_player
from streamlit_extras.let_it_rain import rain



# Streamlit app
def main():
    st.title("Welcome to the Human-Data Interaction simulator")
    st.subheader('Ready to dance with your data ?')

    # Embed a music from SoundCloud
    st_player("https://soundcloud.com/ristanuizuksh/sets/disclosure-you-and-me-flume")

    rain(
    emoji="❤️",
    font_size=54,
    falling_speed=4,
    animation_length="infinite",
)


if __name__ == "__main__":
    main()
