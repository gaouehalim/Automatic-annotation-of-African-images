import os
import requests
import pandas as pd
from urllib.request import urlretrieve

def get_images_from_commons(keyword, limit=10):
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": keyword,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|user|extmetadata",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()
    images = []

    pages = data.get("query", {}).get("pages", {})
    for i, page in enumerate(pages.values()):
        info = page.get("imageinfo", [{}])[0]
        meta = info.get("extmetadata", {})
        image = {
            "filename": f"{keyword.replace(' ', '_')}_{i}.jpg",
            "url": info.get("url", ""),
            "description": meta.get("ImageDescription", {}).get("value", "").strip(),
            "category": keyword
        }
        images.append(image)
    return images

def save_images_and_csv(images, download_folder="images", csv_file="images_metadata.csv"):
    os.makedirs(download_folder, exist_ok=True)
    rows = []

    for image in images:
        if not image["url"]:
            continue
        path = os.path.join(download_folder, image["filename"])
        try:
            urlretrieve(image["url"], path)
            print(f"✅ Téléchargé : {image['filename']}")
            rows.append(image)
        except Exception as e:
            print(f"❌ Erreur sur {image['filename']} : {e}")

    # Append au CSV existant
    df = pd.DataFrame(rows)
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', index=False, header=False, encoding="utf-8")
    else:
        df.to_csv(csv_file, index=False, encoding="utf-8")

# --- EXÉCUTION MULTI-MOTS CLÉS ---
if __name__ == "__main__":
    keywords = [
        "village africain",
        "marché africain",
        "fête traditionnelle",
        "paysage sahélien",
        "scène urbaine Afrique",
        "danse africaine",
        "transport en Afrique"
    ]

    for keyword in keywords:
        print(f"\n🔍 Recherche : {keyword}")
        images = get_images_from_commons(keyword, limit=15)
        save_images_and_csv(images)
