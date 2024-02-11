from pdb import run
import streamlit as st
import ollamac.ollamac as ollamac

input = st.text_area('Your question', value='Why is the sky blue?')
click = st.button('Generate')
if click:
    runner = ollamac.OlcRunner()
    runner.host = "localhost"
    runner.port = 8888
    st.write(runner._generate(input))