import requests
import streamlit as st
import base64
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def get_img_as_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_bytes = query({
    "inputs": st.text_input('Enter your prompt'),
})

image = Image.open(io.BytesIO(image_bytes))

if st.button('Generate Image'):
    st.image(image)

img = get_img_as_base64("M:/Guvi/day2/kio.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
