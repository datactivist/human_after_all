import streamlit as st 
from streamlit_player import st_player


# Streamlit app
def main():
    st.title("Welcome to the Human-Data Interaction simulator")
    st.subheader('Ready to dance with your data ?')
    
    # Embed a youtube video
    st_player("https://youtu.be/CmSKVW1v0xM")

    # Embed a music from SoundCloud
    st_player("https://soundcloud.com/imaginedragons/demons")

if __name__ == "__main__":
    main()
