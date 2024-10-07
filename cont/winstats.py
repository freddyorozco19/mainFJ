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

if img:
    if img == images[1]:  # Primera imagen
        # Mostrar la imagen como un enlace
        st.markdown(f'<a href="http://www.winstats.com.ec" target="_blank"><img src="{img}" style="width: 100%;"></a>', unsafe_allow_html=True)
    else:
        st.image(img, caption="Has seleccionado una imagen.")
st.header("WIN STATS")
