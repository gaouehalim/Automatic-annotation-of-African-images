import streamlit as st

def show_about():
    st.title("ℹ️ À propos de ce projet")

    st.markdown("""
    # 🌍 Annotation Automatique d'Images Africaines
    ---

    ## 🎯 Objectif du projet

    Ce projet a été réalisé dans le cadre du **Hackathon Academic Pioneers 2025**, avec pour objectif d'**explorer l'utilisation d'API d'annotation automatique** pour **générer des descriptions textuelles** d'images **représentatives des scènes africaines**.

    Plus précisément, le projet vise à :

    - **Annoter automatiquement** des images africaines en utilisant des modèles de vision pré-entraînés.
    - **Constituer un ensemble d'images** riche et représentatif de la diversité africaine.
    - **Adapter et évaluer** les modèles existants face aux **spécificités culturelles et visuelles** africaines.
    - **Proposer des axes d'amélioration** pour une annotation plus fidèle.

    ---

    ## 🛠️ Démarche et méthodologie

    - **Collecte des données** :
        - Extraction de plus de **1900 images** depuis l'**API Unsplash** sur la base de **60+ mots-clés** ciblant des thématiques africaines (marchés, villages, traditions, paysages, etc.).
        - **Enrichissement manuel** d'une partie du dataset par sélection et annotation d'images rurales spécifiques, pour compenser le manque de représentativité.

    - **Annotation automatique** :
        - Utilisation du modèle **BLIP-2** (Salesforce, HuggingFace) pour générer une description automatique pour chaque image.

    - **Évaluation de la qualité** :
        - Calcul de la **similarité sémantique** entre descriptions humaines (ou enrichies) et annotations automatiques, via **Sentence-Transformers** (`paraphrase-MiniLM-L6-v2`).

    - **Développement d'une application Streamlit** :
        - **Dashboard interactif** pour explorer les statistiques du dataset, visualiser les annotations, et évaluer la qualité globale du modèle.
        - **Module Upload** pour permettre l'annotation d'images extérieures.

    ---

    ## 🧰 Outils et technologies utilisés

    | Outil / Technologie | Rôle |
    |:---------------------|:---------------------------|
    | **Streamlit** | Développement de l'application interactive |
    | **BLIP-2 (Transformers)** | Génération d'annotations |
    | **Sentence-Transformers** | Évaluation de similarité |
    | **Pandas** | Traitement et manipulation de données |
    | **Plotly** | Visualisations interactives |
    | **Unsplash API** | Source principale d'images africaines |

    ---

    ## 📊 Résultats clés

    - **Nombre total d'images** : 1947
    - **Taux moyen de similarité** : environ 0.46/1.00 selon ma dernière évaluation.
    - **Tendances observées** :
        - Très bonnes annotations sur les **paysages naturels** et **scènes urbaines simples**.
        - Difficultés sur les **contextes culturels fins** (festivals, vêtements traditionnels).

    ---

    ## 📈 Conclusions et recommandations

    - **BLIP-2** offre une **base solide** pour l'annotation d'images africaines.
    - Cependant, des **lacunes apparaissent** dès qu'il s'agit de **contextes culturels complexes** ou **ruraux spécifiques**.
    - Pour améliorer les performances :
        - **Constituer un dataset étiqueté manuellement** spécifiquement africain.
        - **Réaliser un fine-tuning** du modèle sur ce dataset enrichi.
        - **Ajouter des métadonnées culturelles** pour guider l'annotation automatique.

    ---

    ## 🔮 Perspectives d'avenir

    - Construction d'une **base de données d'images africaines labellisées** (open dataset).
    - **Spécialisation des modèles** sur des **contextes culturels sous-représentés**.
    - Déploiement d'une application d'annotation **grand public** adaptée aux besoins africains.

    ---

    **Réalisé par : [GAOUE SEIDOU Halimou]  
    Hackathon Academic Pioneers 2025**
    """)
