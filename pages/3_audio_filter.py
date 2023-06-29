import streamlit as st
from streamlit_lottie import st_lottie

def app():
    st.title("Duck talk")
    st.subheader('Tell yourself about what you want to do with what yo do')

    st.markdown('Corneille wrote in Polyeucte : "A raconter ses maux, souvent on les soigne", which means that talking to ourselves very often enlightens our problems and gives us key to solve them. Developers talk about the Rubber duck debugging technique 🦆')
    

    st_lottie("https://assets7.lottiefiles.com/packages/lf20_Wb5prVKFMW.json")


if __name__ == "__main__":
    app()
