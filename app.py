import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
import os
from transformers import pipeline


#Creating the GUI for webpage
with st.sidebar:
    st.title("PDF chat App")
    st.markdown('''
    ## About
    This app is an LLM powered chatbot biult using:
    - [Streamlit](https://streamlit.io/)
    - [Huggingface](https://huggingface.co/docs/transformers/model_doc/bert#bertforquestionanswering)
    - [Huggindface models](https://huggingface.co/models) LLM model
    ''')
    add_vertical_space(5)
    st.write('Made by Developer')

# Creating main fucntion for the uploading the pdf format and model weigths
def main():
    st.header('Chat with PDF ')
    

    # upload a PDF file 
    pdf = st.file_uploader('Upload your PDF', type = 'pdf')
    if pdf is not None:
        st.write(pdf.name)
    else:
        st.write("pdf is None")

    
    #Reading PDF file and extracting the text from the file
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        # st.write(pdf_reader)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
        st.subheader("PDF Uploaded Successfully:")
        
        
        #Loading the BERT model
        embeddings = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
           
        #Accept user questions
        query = st.text_input("Ask question from your PDF file:")
        st.write(query)
        if query:
        # Use the question-answering model
            answer = embeddings(context=text, question=query)
            st.subheader("Bot's Answer:")
            st.write(answer["answer"])


if __name__== '__main__':
    main()
