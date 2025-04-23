# app/prepare_data.py

import pandas as pd

@st.cache_data
def load_metadata():
    """Charge les métadonnées des images."""
    metadata_path = "../african_data_collector/storage/meta_images_final.csv"  # <-- Corrige ici si besoin
    return pd.read_csv(metadata_path)

@st.cache_data
def load_annotations():
    """Charge les annotations générées."""
    annotations_path = "../annotation/storage/annotations_blip2.csv"  # <-- Corrige ici si besoin
    return pd.read_csv(annotations_path)
