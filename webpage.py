import requests
import io
import base64
import streamlit as st
from PIL import Image

st.title("Medical Segmentation")

uploaded_file = st.file_uploader("UNet Segmentation Model", accept_multiple_files=False, type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.subheader("Uploaded Images")
    image = Image.open(uploaded_file)
    st.image(image, caption=uploaded_file.name, width=256)


if st.button("Submit"):
    files = {"image": uploaded_file.getbuffer()}
    response = requests.post("http://localhost:5000//model", files=files)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            pred_image_base64 = data["image"]
            pred_image_bytes = base64.b64decode(pred_image_base64)
            pred_image = Image.open(io.BytesIO(pred_image_bytes))
            
            st.subheader("Predicted Image")
            original_image = Image.open(uploaded_file)
            original_image_resized = original_image.resize(pred_image.size)
            original_image_rgba = original_image_resized.convert("RGBA")
            pred_image_rgba = pred_image.convert("RGBA")
            blended_image = Image.blend(original_image_rgba, pred_image_rgba, alpha=0.5)

            col1, col2= st.columns(2) 
            with col1:
                st.image(blended_image, caption="Blended Segmentation", width=256)
            with col2:
                st.image(pred_image, caption="Segmentation Mask", width=256)
            

            # st.subheader("Blended Image (Original + Segmentation Mask)")
            # st.image(original_image, caption="Original Image", width=256)
            # st.image(pred_image, caption="Segmentation Mask", width=256)
            
        