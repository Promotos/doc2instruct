import streamlit as st
import ollamac.ollamac as ollamac
import numpy as np
import pandas as pd
from pypdf import PdfReader


def extract_text(input_file):        
    reader = PdfReader(input_file)
    text = ''
    for page in reader.pages:
        text += '\n' + page.extract_text()
    
    return text


st.subheader('Document to Instruction Data Set')

input_file = st.file_uploader("Choose a input file", type=['pdf'], accept_multiple_files=False, help='Select a input file to be processed as instruction set.')
btn_extract_text = st.button('Extract Text')

if btn_extract_text:
    with st.status("Processing...", expanded=True):
        st.write("Extract Text...")
        text = extract_text(input_file)
        st.download_button(
                label="Download data as text",
                data=text,
             file_name='text.txt',
             mime='text/text'
        )


#if input_file is not None:
    
        #input_file.getvalue
        #elements = partition_pdf("examples/fritzbox-7590_man_en_GB.pdf")
        #print(elements)
        
        #st.write("Searching for data...")
        #time.sleep(2)
        #st.write("Found URL.")
        #time.sleep(1)
        #st.write("Downloading data...")
        #time.sleep(1)
        
            #text = extract_text()
        


#input = st.text_area('Your question', value='Why is the sky blue?')
#click = st.button('Generate')
#if click:
#    runner = ollamac.OlcRunner()
#    runner.host = "localhost"
#    runner.port = 8888
#    st.write(runner._generate(input))