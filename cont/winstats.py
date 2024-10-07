import streamlit as st
from streamlit_image_select import image_select


img = image_select(
    label="Select a cat",
    images=[
        "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg",
        "https://bagongkia.github.io/react-image-picker/0759b6e526e3c6d72569894e58329d89.jpg"
    ],
    captions=["A cat", "Guess what, a cat..."],
)
st.write(img)

st.header("WIN STATS")
