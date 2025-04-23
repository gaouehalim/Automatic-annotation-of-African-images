import streamlit as st
from modules.dashboard import show_dashboard
from modules.upload import show_upload
from modules.about import show_about

st.set_page_config(page_title="Annotation Automatique de Scènes Africaines", page_icon="🌍", layout="wide")

# Sidebar styling
st.sidebar.title("🌍 Annotation Africaine")
st.sidebar.markdown("---")

# Menu principal
menu = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Dashboard", "📤 Uploader une Image", "ℹ️ À propos"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Projet Hackathon 2025 - Pioneers 🚀")

if menu == "🏠 Dashboard":
    show_dashboard()

elif menu == "📤 Uploader une Image":
    show_upload()

elif menu == "ℹ️ À propos":
    show_about()
