import streamlit as st
from streamlit_image_select import image_select
from PIL import Image

st.header("WIN STATS")
st.image("Resources/Img/wyscoutlogo.png")

# Cargar una imagen
image = Image.open("Resources/Img/wyscoutlogo.png")

# Función para convertir la imagen a base64
def image_to_base64(image):
    import io
    import base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str
# Mostrar la imagen con un marco
st.markdown(
    f"""
    <div style="border: 5px solid #4CAF50; padding: 10px; display: inline-block;">
        <img src="data:image/jpeg;base64,{image_to_base64(image)}" style="width: 100%;">
    </div>
    """,
    unsafe_allow_html=True
)


