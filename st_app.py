from typing import List
import streamlit as st
import ollamac.ollamac as ollamac
import numpy as np
import pandas as pd
from pypdf import PdfReader
from semantic_text_splitter import CharacterTextSplitter

def split_text(text, max_characters = 1024) -> List[str]:
    splitter = CharacterTextSplitter(trim_chunks=True)
    return splitter.chunks(text, max_characters)


def extract_text(input_file) -> str:        
    reader = PdfReader(input_file)
    text = ''
    for page in reader.pages:
        text += '\n' + clean(page.extract_text())
    
    return text

def clean(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped).strip()

st.subheader('Document to Instruction Data Set')

input_file = st.file_uploader("Choose a input file", type=['pdf'], accept_multiple_files=False, help='Select a input file to be processed as instruction set.')

if input_file is not None:
    col1, col2 = st.tabs(['Extract Text','Extract & Split Text'])

    btn_extract_text = col1.button('Extract Text')

    chunk_max_char = col2.number_input('Chunk Size', value=1024)
    btn_split_text = col2.button('Split Text')

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

    if btn_split_text:
        with st.status("Processing...", expanded=True):
            st.write("Extract Text...")
            text = extract_text(input_file)
            
            st.write("Split Text...")
            chunks = split_text(text, max_characters=chunk_max_char)
            print(chunks[2])

            df = pd.DataFrame(chunks, columns=['chunks'])
            
            st.download_button(
                    label="Download data as csv",
                    data=df.to_csv(index=False),
                file_name='chunks.csv',
                mime='text/csv'
            )    