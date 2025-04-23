import pandas as pd
import glob

fichiers_csv = ['african_data_collector/storage/meta_images2.csv', 'african_data_collector/storage/meta_images1.csv', 'african_data_collector/storage/meta_images.csv']

df_combines = pd.concat([pd.read_csv(fichier) for fichier in fichiers_csv], ignore_index=True)

df_combines.to_csv('african_data_collector/storage/meta_images_final.csv', index=False)

print("Fusion terminée. Fichier créé : fusion_resultat.csv")
