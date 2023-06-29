import streamlit as st 
from streamlit_player import st_player
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo



# Streamlit app
def main():
    #set title of the app
    st.title("Welcome to the Human-Data Interaction simulator")
    #add some animation to make the user feel he will be using a very special kind of artefact.
    rain(
    emoji="🕺",
    font_size=40,
    falling_speed=4,
    animation_length="infinite",
)
    #add a logo
    add_logo("gallery/logo_dataflow_vf.png", height=100)
    
    #add a subheader
    st.subheader('Ready to dance with your data ?')

    #write the welcome text
    st.write('Hello and welcome to the Human-Data Interaction (HDI) simulator. Before we begin, take time to settle down, make yourself comfortable, listen to the music below ⬇️')

    # Add some ambiance sound
    st_player("https://soundcloud.com/ristanuizuksh/sets/disclosure-you-and-me-flume")

    #add some text
    st.write('Feeling better ? Now you can start whenever you want !')
    
    next_page = st.button("Begin 🍾 ! ")
    if next_page:
        switch_page("Let's go ⏯️ !")

if __name__ == "__main__":
    main()
