# 🌍 Automatic Annotation of African Scenes

## 📜 Présentation

Ce projet vise à automatiser l'annotation d'images représentant des **scènes africaines** à l'aide de modèles de vision modernes.  
L'objectif est de **réduire le biais culturel** dans les datasets d'images, en générant des annotations mieux adaptées aux spécificités africaines.

---

## 🎯 Objectifs

- **Collecter** un dataset riche et varié d'images africaines.
- **Annoter automatiquement** ces images avec un modèle de vision de pointe (**BLIP-2**).
- **Évaluer la qualité** des annotations générées en les comparant aux descriptions humaines.
- **Développer une interface utilisateur** intuitive pour visualiser et interagir avec les résultats.

---

## 🏛️ Structure du projet

├── african_data_collector/ │
  ├── data_collection.py → collecte d'images via API Unsplash │ 
  ├── data_cleaning.py → nettoyage et formatage des données collectées │ 
  ├── data_analysis.py → analyse statistique du dataset │
  ├── fusion.py → fusion et préparation finale du dataset
├── annotation/ │
  └── blip2_annotator/ │ 
      └── blip2_annotator.py → annotation automatique avec BLIP-2 
├── evalution/ │
  └── compare_annotations_bert.ipynb → évaluation de la similarité sémantique
├── app/ │ 
  ├── main.py → application Streamlit │ 
  ├── modules/ → pages du dashboard (dashboard, upload, about) │ 
  ├── data/ → résultats finaux (annotations + scores) 
├── requirements.txt → dépendances 
├── README.md


---

## 🛠️ Outils et technologies utilisés

| Outil / Technologie        | Utilisation |
|:---------------------------|:------------|
| **Unsplash API**            | Collecte d'images africaines |
| **Pandas**                  | Manipulation de données |
| **Streamlit**               | Développement d'une interface utilisateur web |
| **BLIP-2 (Salesforce)**      | Génération automatique d'annotations |
| **Sentence-Transformers**   | Évaluation de la qualité d'annotations |
| **Plotly**                  | Visualisations interactives |

---

## 📊 Détail du Dataset

- **Nombre d'images collectées** : ~1964
- **Thématiques couvertes** :
  - Scènes naturelles (savane, désert, forêts)
  - Vie urbaine et rurale
  - Vie culturelle (fêtes, traditions, artisanat)
- **Provenance** : Unsplash (recherche ciblée sur mots-clés africains)
- **Nettoyage** : Suppression des doublons, des images non pertinentes.

**Dataset final** :  
- 1947 images prêtes pour annotation et évaluation.
- Chaque image dispose :
  - d'une **description humaine** (métadonnée Unsplash)
  - d'une **annotation automatique** (générée par BLIP-2)
  - d'un **score de similarité sémantique** (0 à 1).

---

## 🚀 Lancer l'application

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/gaouehalim/Automatic-annotation-of-African-images.git
    cd Automatic-annotation-of-African-images
    ```

2. Installer les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Démarrer Streamlit :
    ```bash
    streamlit run app/main.py
    ```

---

## 📈 Résultats

- **Score moyen de similarité** : environ 0.46/1.00 selon ma dernière évaluation.
- **Forces** :
  - Très bonne annotation des scènes naturelles (paysages, animaux).
- **Faiblesses** :
  - Difficulté pour des concepts culturels complexes (ex : objets traditionnels rares).

---

## 📢 Conclusion

Le modèle BLIP-2 fournit des résultats **très encourageants** pour des scènes génériques.  
Cependant, une **spécialisation (fine-tuning)** est nécessaire pour atteindre un niveau expert sur des contenus **culturellement riches et spécifiques à l'Afrique**.

Ce projet démontre l'importance de :
- Construire des datasets **spécifiques et représentatifs**.
- Adapter les modèles d'IA aux **diversités culturelles**.

---

## 👤 Auteur

Projet réalisé par **GAOUE SEIDOU Halimou**  
Hackathon Academic Pioneers 2025

---

