import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():
    st.title("🏠 Dashboard - Analyse du Dataset")

    # Charger le fichier final
    df = pd.read_csv("/home/pionner01/Automatic-annotation-of-African-images/app/data/resultats_similarite.csv")

    # ➡️ Section Informations sur le Dataset
    st.header("🗂️ Description du Dataset")
    st.markdown("""
    - **Origine** : Images collectées via API Unsplash, enrichies manuellement.
    - **Mots-clés utilisés** : Plus de 60 thématiques ciblant la culture, la vie quotidienne et les paysages africains.
    - **Taille du Dataset** : Plus de 1964 images annotées.
    - **Métadonnées disponibles** : 
        - `filename` (Nom du fichier)
        - `description` (Description humaine)
        - `annotation` (Annotation automatique)
        - `category` (Thématique associée)
    - **Particularité** : Une partie du dataset a été manuellement enrichie pour refléter fidèlement les réalités rurales et culturelles africaines.
    """)
    st.write("---")

    st.header("📊 Informations Générales")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Nombre d'images", len(df))
    with col2:
        st.metric("Score moyen", f"{df['similarity_score'].mean():.2f}")
    with col3:
        st.metric("Score max", f"{df['similarity_score'].max():.2f}")

    st.write("---")
    
    st.subheader("🔍 Aperçu aléatoire des annotations")
    samples = df.sample(5)
    for _, row in samples.iterrows():
        st.image(f"/home/pionner01/Automatic-annotation-of-African-images/african_data_collector/storage/images/{row['filename']}", width=300)
        st.write(f"**Description humaine :** {row['description']}")
        st.write(f"**Annotation automatique :** {row['annotation']}")
        st.write(f"**Score de similarité :** {row['similarity_score']:.2f}")
        st.markdown("---")

    st.write("## 📈 Distribution des Scores de Similarité")
    fig = px.histogram(df, x="similarity_score", nbins=30, title="Distribution des Similarités")
    st.plotly_chart(fig, use_container_width=True)

    st.write("## 🧹 Explorer les cas faibles")
    seuil = st.slider("Seuil de score minimal", 0.0, 1.0, 0.5, 0.01)
    mauvais = df[df['similarity_score'] < seuil]
    st.write(f"{len(mauvais)} images avec un score < {seuil}")

    if not mauvais.empty:
        for _, row in mauvais.iterrows():
            st.image(f"/home/pionner01/Automatic-annotation-of-African-images/african_data_collector/storage/images/{row['filename']}", width=300)
            st.write(f"**Description humaine :** {row['description']}")
            st.write(f"**Annotation automatique :** {row['annotation']}")
            st.write(f"**Score :** {row['similarity_score']:.2f}")
            st.markdown("---")

    st.write("## 🎯 Taux de Bonnes Annotations")
    seuil_bon = 0.7
    bonnes = len(df[df['similarity_score'] >= seuil_bon])
    mauvaises = len(df[df['similarity_score'] < seuil_bon])
    fig_pie = px.pie(
        names=["Bonnes annotations", "Annotations faibles"],
        values=[bonnes, mauvaises],
        title=f"Annotations (Seuil {seuil_bon})"
    )
    st.plotly_chart(fig_pie, use_container_width=True)
