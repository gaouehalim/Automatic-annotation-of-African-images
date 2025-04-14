import os
import requests

def download_image(url, save_path):
    try:
        img_data = requests.get(url).content
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Image téléchargée à {save_path}")
    except Exception as e:
        print(f"Erreur de téléchargement : {e}")

def create_dir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
