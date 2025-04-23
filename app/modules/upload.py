import streamlit as st
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration

@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b", use_fast=True)
    model = Blip2ForConditionalGeneration.from_pretrained(
        "Salesforce/blip2-opt-2.7b",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    model.to(device)
    return processor, model, device

def show_upload():
    st.title("📤 Uploader une Image pour Annotation")

    uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Image uploadée", use_column_width=True)

        if st.button("Générer une annotation"):
            with st.spinner("Génération de l'annotation..."):
                processor, model, device = load_model()
                inputs = processor(images=image, return_tensors="pt").to(device)
                generated_ids = model.generate(**inputs)
                generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
                st.success("Annotation générée :")
                st.write(f"**{generated_text}**")
