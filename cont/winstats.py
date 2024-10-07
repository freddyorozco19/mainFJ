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

# Dimensiones de la primera imagen
new_width = 2061  # Manteniendo el ancho de la segunda imagen
new_height = int((29 / 35) * new_width)  # Calculando el alto para la relación 35:29
# Redimensionar la imagen
resized_image = image1.resize((new_width, new_height), Image.LANCZOS)
# Convertir a RGB si la imagen tiene un canal alfa
if resized_image.mode == "RGBA":
    resized_image = resized_image.convert("RGB")

# Guardar la nueva imagen
resized_image.save("resized_image.jpg", "JPEG")

# Mostrar la nueva imagen (opcional)
resized_image.show()
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
    # Mostrar la imagen con un marco
    st.markdown(
        f"""
        <div style="border: 5px solid #FF0046; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{image_to_base64(resized_image)}" style="width: 100%;">
        </div>
        """,
        unsafe_allow_html=True
    )
with imgmn02:
    # Mostrar la imagen con un marco
    st.markdown(
        f"""
        <div style="border: 5px solid #FF0046; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{image_to_base64(image2)}" style="width: 100%;">
        </div>
        """,
        unsafe_allow_html=True
    )


