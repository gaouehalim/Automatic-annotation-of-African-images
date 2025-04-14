import pandas as pd

class DataCleaner:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(csv_file)

    def remove_duplicates(self):
        self.df.drop_duplicates(subset=['image_url'], inplace=True)

    def remove_missing_data(self):
        self.df.dropna(subset=['description', 'image_url'], inplace=True)

    def save_cleaned_data(self):
        self.df.to_csv(self.csv_file, index=False)
