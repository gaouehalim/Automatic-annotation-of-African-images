import os
import torch
import pandas as pd
from PIL import Image
from tqdm import tqdm
from transformers import Blip2Processor, Blip2ForConditionalGeneration

# Chargement du modèle BLIP-2
print("Chargement du modèle BLIP-2...")
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b", use_fast=True)
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16 if device == "cuda" else torch.float32)
model.to(device)
print("Modèle chargé sur", device)

def annotate_images_blip2(image_folder, output_csv="annotation/storage/annotations_blip2.csv"):
    annotations = []

    # Charger les annotations existantes si elles existent
    if os.path.exists(output_csv):
        existing_annotations = pd.read_csv(output_csv)
        already_annotated = set(existing_annotations['image_name'])
        print(f"🔎 {len(already_annotated)} images déjà annotées, reprise du processus...")
    else:
        existing_annotations = pd.DataFrame(columns=["image_name", "annotation"])
        already_annotated = set()

    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    for image_name in tqdm(image_files, desc="Annotation des images"):
        if image_name in already_annotated:
            continue  # Sauter les images déjà annotées

        image_path = os.path.join(image_folder, image_name)
        try:
            image = Image.open(image_path).convert("RGB")
        except Exception as e:
            print(f"Erreur ouverture {image_name}: {e}")
            continue

        inputs = processor(images=image, return_tensors="pt").to(device)
        generated_ids = model.generate(**inputs, max_new_tokens=1000)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

        annotations.append({
            "image_name": image_name,
            "annotation": generated_text
        })

        # Sauvegarder immédiatement après chaque annotation pour éviter la perte en cas d'arrêt
        temp_df = pd.DataFrame(annotations)
        final_df = pd.concat([existing_annotations, temp_df], ignore_index=True)
        final_df.to_csv(output_csv, index=False)

        # Mettre à jour la liste des images annotées
        existing_annotations = final_df
        already_annotated.add(image_name)
        annotations = []  # Réinitialiser la liste pour ne pas la doubler

    print(f"✅ Annotation terminée. Résultats dans {output_csv}")

if __name__ == "__main__":
    dossier_images = "/home/pionner01/Automatic-annotation-of-African-images/african_data_collector/storage/images"
    annotate_images_blip2(dossier_images)


# import os
# import torch
# import pandas as pd
# from PIL import Image
# from torchvision import transforms
# from tqdm import tqdm
# from transformers import Blip2Processor, Blip2ForConditionalGeneration

# # Chargement du modèle BLIP-2
# print("Chargement du modèle BLIP-2...")
# device = "cuda" if torch.cuda.is_available() else "cpu"
# processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b", use_fast=True)
# model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16 if device == "cuda" else torch.float32)
# model.to(device)
# print("Modèle chargé sur", device)

# def annotate_images_blip2(image_folder, output_csv="annotation/storage/annotations_blip2.csv"):
#     annotations = []

#     image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
#     for image_name in tqdm(image_files, desc="Annotation des images"):
#         image_path = os.path.join(image_folder, image_name)
#         image = Image.open(image_path).convert("RGB")

#         inputs = processor(images=image, return_tensors="pt").to(device)
#         generated_ids = model.generate(**inputs)
#         generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

#         annotations.append({
#             "image_name": image_name,
#             "annotation": generated_text
#         })

#     df = pd.DataFrame(annotations)
#     df.to_csv(output_csv, index=False)
#     print(f"📄 Annotations sauvegardées dans {output_csv}")

# if __name__ == "__main__":
#     dossier_images = "/home/pionner01/Automatic-annotation-of-African-images/african_data_collector/storage/images"  # ← Remplace ce chemin
#     annotate_images_blip2(dossier_images)
# import os
# import torch
# import pandas as pd
# from PIL import Image
# from torchvision import transforms
# from tqdm import tqdm
# from transformers import Blip2Processor, Blip2ForConditionalGeneration

# # Chargement du modèle BLIP-2
# print("🔄 Chargement du modèle BLIP-2...")
# device = "cuda" if torch.cuda.is_available() else "cpu"
# processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b", use_fast=True)
# model = Blip2ForConditionalGeneration.from_pretrained(
#     "Salesforce/blip2-opt-2.7b", 
#     torch_dtype=torch.float16 if device == "cuda" else torch.float32
# )
# model.to(device)
# print("✅ Modèle chargé sur", device)

# def annotate_first_n_images(image_folder, output_csv="annotation/storage/annotations_blip2.csv", n=100):
#     annotations = []

#     image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))])[:n]

#     for image_name in tqdm(image_files, desc=f"🔍 Annotation des {n} premières images"):
#         image_path = os.path.join(image_folder, image_name)
#         image = Image.open(image_path).convert("RGB")

#         inputs = processor(images=image, return_tensors="pt").to(device)
#         generated_ids = model.generate(**inputs)
#         generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

#         annotations.append({
#             "image_name": image_name,
#             "annotation": generated_text
#         })

#     df = pd.DataFrame(annotations)
#     os.makedirs(os.path.dirname(output_csv), exist_ok=True)
#     df.to_csv(output_csv, index=False)
#     print(f"📄 Annotations sauvegardées dans {output_csv}")

# if __name__ == "__main__":
#     dossier_images = "/home/pionner01/Automatic-annotation-of-African-images/african_data_collector/storage/images"
#     annotate_first_n_images(dossier_images, n=100)
