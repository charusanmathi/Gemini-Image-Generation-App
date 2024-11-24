from dotenv import load_dotenv
load_dotenv()  #loading all environment variables


import streamlit as st
import os 
from PIL import Image

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini model and get response

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response= model.generate_content(image)
    return response.text


# Initialise the streamlit app

st.set_page_config(page_title="Gemini Image Geneartion")

st.header("Gemini Image Generation App")

input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image..",type = ['png','jpeg','jpg'])

image = ""

if uploaded_file is not None: 
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Tell me about the image")

# If submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The response is: ")
    st.write(response)