import os
import requests
import csv
from dotenv import load_dotenv

load_dotenv()

class ImageCollector:
    def __init__(self, access_key, search_terms, images_per_term, save_dir, csv_file):
        self.access_key = access_key
        self.search_terms = search_terms
        self.images_per_term = images_per_term
        self.save_dir = save_dir
        self.csv_file = csv_file

    def collect_images(self):
        os.makedirs(self.save_dir, exist_ok=True)
        with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['filename', 'description', 'image_url', 'category'])
            for term in self.search_terms:
                print(f"Recherche de : {term}")
                url = f'https://api.unsplash.com/search/photos?query={term}&per_page={self.images_per_term}&client_id={self.access_key}'
                response = requests.get(url)
                data = response.json()
                self._process_images(data, term, writer)

    def _process_images(self, data, category, writer):
        for i, img in enumerate(data.get('results', [])):
            img_url = img['urls']['regular']
            description = img.get('description') or img.get('alt_description') or 'N/A'
            filename = f"{category.replace(' ', '_')}_{i}.jpg"
            filepath = os.path.join(self.save_dir, filename)
            self._download_image(img_url, filepath)
            writer.writerow([filename, description, img_url, category])
            print(f"✅ Image {filename} enregistrée.")

    def _download_image(self, img_url, filepath):
        with open(filepath, 'wb') as img_file:
            img_file.write(requests.get(img_url).content)
