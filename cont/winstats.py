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

# Verifica si se ha seleccionado una imagen
if img:
    # Abre el enlace específico en una nueva pestaña
    st.markdown('<a href="http://www.winstats.com.ec" target="_blank">Ir a Win Stats</a>', unsafe_allow_html=True)
st.header("WIN STATS")
