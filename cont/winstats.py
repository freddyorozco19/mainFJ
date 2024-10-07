import streamlit as st
from streamlit_image_select import image_select
from PIL import Image
import io
import base64

st.header("WIN STATS")
st.image("Resources/Img/wyscoutlogo.png")

# Cargar una imagen
image1 = Image.open("Resources/Img/wyscoutlogo.png")
image2 = Image.open("Resources/Img/optalogo.png")
image3 = Image.open("Resources/Img/fbreflogo.png")

# Obtener dimensiones de la segunda imagen
new_width, new_height = image2.size  # Ancho y alto de la segunda imagen
resized_image1 = image1.resize((new_width, new_height), Image.LANCZOS)
if resized_image.mode == "RGBA":
    resized_image = resized_image1.convert("RGB")
resized_image1.save("Resources/Img/resized_wyscoutlogo.png")  # Cambia el nombre según necesites
resized_image1.show()

resized_image2 = image3.resize((new_width, new_height), Image.LANCZOS)
if resized_image2.mode == "RGBA":
    resized_image2 = resized_image2.convert("RGB")
resized_image2.save("Resources/Img/resized_fbreflogo.png")  # Cambia el nombre según necesites
resized_image2.show()



# Función para convertir la imagen a base64
def image_to_base64(image):
    buffered = io.BytesIO()
    # Cambiar el formato a PNG si la imagen tiene un canal alfa
    if image.mode == "RGBA":
        image = image.convert("RGB")  # Convertir a RGB para JPEG
    image.save(buffered, format="PNG")  # Guarda como PNG
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str


imgmn01, imgmn02, imgmn03 = st.columns(3)
with imgmn01:
    st.markdown(
        f"""
        <div style="border: 4px solid #FF0046; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{image_to_base64(resized_image)}" style="width: 100%;">
        </div>
        """,
        unsafe_allow_html=True
    )
with imgmn02:
    st.markdown(
        f"""
        <div style="border: 4px solid #FF0046; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{image_to_base64(image2)}" style="width: 100%;">
        </div>
        """,
        unsafe_allow_html=True
    )
with imgmn03:
    st.markdown(
        f"""
        <div style="border: 4px solid #FF0046; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{image_to_base64(resized_image2)}" style="width: 100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

