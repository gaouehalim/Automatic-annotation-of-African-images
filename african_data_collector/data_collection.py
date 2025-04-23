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
                # On définit le nombre total d'images à récupérer
                total_images = self.images_per_term
                images_collected = 0
                page = 1

                while images_collected < total_images:
                    url = f'https://api.unsplash.com/search/photos?query={term}&per_page=30&page={page}&client_id={self.access_key}'
                    response = self._get_request(url)
                    if response:
                        data = response.json()
                        self._process_images(data, term, writer)
                        images_collected += len(data['results'])
                        page += 1
                    else:
                        break

    def _get_request(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
            elif response.status_code == 403:
                print("🔴 API Rate Limit Exceeded. Waiting for 1 minute.")
                time.sleep(60) 
                return self._get_request(url)
            else:
                print(f"❌ Failed to fetch data. Status Code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None

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
        try:
            with open(filepath, 'wb') as img_file:
                img_file.write(requests.get(img_url).content)
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to download image: {e}")
