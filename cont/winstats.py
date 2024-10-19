import streamlit as st
from streamlit_image_select import image_select
from PIL import Image
import io
import base64

st.header("WIN STATS")
st.divider()
# Cargar una imagen
image1 = Image.open("Resources/Img/wyscoutlogo.png")
image2 = Image.open("Resources/Img/optalogo.png")
image3 = Image.open("Resources/Img/fbreflogo.png")
image4 = Image.open("Resources/Img/winstatslogo.png")
image5 = Image.open("Resources/Img/FootballDivisionWorldwide-removebg-preview.png")

link_url1 = "https://wyscoutdata.streamlit.app"
link_url2 = "https://opproccesdata.streamlit.app"
link_url3 = "https://fbrefdata.streamlit.app"
link_url4 = "https://winstats-chilefem.streamlit.app"
link_url5 = "https://agencyfd-winstats.streamlit.app"

# Obtener dimensiones de la segunda imagen
new_width, new_height = image2.size  # Ancho y alto de la segunda imagen
resized_image1 = image1.resize((new_width, new_height), Image.LANCZOS)
if resized_image1.mode == "RGBA":
    resized_image1 = resized_image1.convert("RGB")
resized_image1.save("Resources/Img/resized_wyscoutlogo.png")  # Cambia el nombre según necesites
resized_image1.show()

resized_image2 = image3.resize((new_width, new_height), Image.LANCZOS)
if resized_image2.mode == "RGBA":
    resized_image2 = resized_image2.convert("RGB")
resized_image2.save("Resources/Img/resized_fbreflogo.png")  # Cambia el nombre según necesites
resized_image2.show()

resized_image4 = image4.resize((new_width, new_height), Image.LANCZOS)
if resized_image4.mode == "RGBA":
    resized_image4 = resized_image4.convert("RGB")
resized_image4.save("Resources/Img/resized_fbreflogo.png")  # Cambia el nombre según necesites
resized_image4.show()

resized_image5 = image5.resize((new_width, new_height), Image.LANCZOS)
if resized_image5.mode == "RGBA":
    resized_image5 = resized_image5.convert("RGB")
resized_image5.save("Resources/Img/resized_fbreflogo.png")  # Cambia el nombre según necesites
resized_image5.show()


def image_to_base64(image):
    buffered = io.BytesIO()
    # Cambiar el formato a PNG si la imagen tiene un canal alfa
    if image.mode == "RGBA":
        image = image.convert("RGB")  # Convertir a RGB para JPEG
    image.save(buffered, format="PNG")  # Guarda como PNG
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Convertir image1 a base64
image1_base64 = image_to_base64(image2)
image2_base64 = image_to_base64(resized_image1)
image3_base64 = image_to_base64(resized_image2)
image4_base64 = image_to_base64(resized_image4)
image5_base64 = image_to_base64(resized_image5)


imgmn01, imgmn02, imgmn03 = st.columns(3)
with imgmn01:
    st.markdown(
        f"""
        <a href="{link_url1}" target="_blank">
            <div style="border: 1px solid #9F9F9F; padding: 5px; display: inline-block;">
                <img src="{image2_base64}" style="width: 100%;">
            </div>
        </a>
        """, unsafe_allow_html=True)
with imgmn02:
    st.markdown(
        f"""
        <a href="{link_url2}" target="_blank">
            <div style="border: 1px solid #9F9F9F; padding: 5px; display: inline-block;">
                <img src="{image1_base64}" style="width: 100%;">
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
with imgmn03:
    st.markdown(
        f"""
        <a href="{link_url3}" target="_blank">
            <div style="border: 1px solid #9F9F9F; padding: 5px; display: inline-block;">
                <img src="{image3_base64}" style="width: 100%;">
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
st.markdown("<br>", unsafe_allow_html=True)
imgmn04, imgmn05, imgmn06 = st.columns(3)
with imgmn04:
    st.markdown(
        f"""
        <a href="{link_url4}" target="_blank">
            <div style="border: 1px solid #9F9F9F; padding: 5px; display: inline-block;">
                <img src="{image4_base64}" style="width: 100%;">
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
with imgmn05:
    st.markdown(
        f"""
        <a href="{link_url5}" target="_blank">
            <div style="border: 1px solid #9F9F9F; padding: 5px; display: inline-block;">
                <img src="{image5_base64}" style="width: 100%;">
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
st.divider()
