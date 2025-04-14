import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def analyze_categories(self):
        category_count = self.df['category'].value_counts()
        print(category_count)

    def visualize_images(self, category):
        # Code pour afficher des échantillons d'images pour une catégorie donnée
        pass

    def analyze_description_length(self):
        self.df['description_length'] = self.df['description'].apply(len)
        print(self.df[['filename', 'description_length']].sort_values(by='description_length', ascending=False).head())
