import streamlit as st
from streamlit_lottie import st_lottie

def app():
    st.title("Meet your copilot")
    st.subheader('Enough of talking to data, meet your copilot and collaborate with some human')
    st_lottie("https://assets10.lottiefiles.com/packages/lf20_Wb5prVKFMW.json", height=300)

    st.markdown('Corneille wrote in Polyeucte : "A raconter ses maux, souvent on les soigne", which means that talking to ourselves very often enlightens our problems and gives us key to solve them. Developers talk about the Rubber duck debugging technique 🦆')
    

    


if __name__ == "__main__":
    app()
