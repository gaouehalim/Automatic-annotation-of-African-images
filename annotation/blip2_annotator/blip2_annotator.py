import os
import torch
import pandas as pd
from PIL import Image
from torchvision import transforms
from tqdm import tqdm
from transformers import Blip2Processor, Blip2ForConditionalGeneration

# Chargement du modèle BLIP-2
print("🔄 Chargement du modèle BLIP-2...")
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b", use_fast=True)
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16 if device == "cuda" else torch.float32)
model.to(device)
print("✅ Modèle chargé sur", device)

def annotate_images_blip2(image_folder, output_csv="annotation/storage/annotations_blip2.csv"):
    annotations = []

    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
    for image_name in tqdm(image_files, desc="🔍 Annotation des images"):
        image_path = os.path.join(image_folder, image_name)
        image = Image.open(image_path).convert("RGB")

        inputs = processor(images=image, return_tensors="pt").to(device)
        generated_ids = model.generate(**inputs)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

        annotations.append({
            "image_name": image_name,
            "annotation": generated_text
        })

    df = pd.DataFrame(annotations)
    df.to_csv(output_csv, index=False)
    print(f"📄 Annotations sauvegardées dans {output_csv}")

if __name__ == "__main__":
    dossier_images = "/home/pionner01/auto-annotation/african_data_collector/storage/benin_image"  # ← Remplace ce chemin
    annotate_images_blip2(dossier_images)
