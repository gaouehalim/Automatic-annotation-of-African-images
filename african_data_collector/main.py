from data_collection import ImageCollector
from data_cleaning import DataCleaner
from data_analysis import DataAnalyzer
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

SEARCH_TERMS = [
    'african village daily life',
    'african city street life',
    'african people in rural areas',
    'traditional african housing',
    'african urban community',
    'african open market scene',
    'african women selling vegetables',
    'african artisans at work',
    'local african shops',
    'african family gathering',
    'african children playing',
    'african elders storytelling',
    'community gathering africa',
    'african classroom in rural area',
    'african students learning',
    'outdoor school africa',
    'african women carrying goods',
    'african bicycle transport',
    'african motorbike taxi',
    'african agriculture workers',
    'african dance ceremony',
    'african music street performance',
    'traditional african wedding',
    'african tribal celebration',
    'african cooking outdoors',
    'african family eating together',
    'traditional food preparation africa'
]

IMAGES_PER_TERM = 200


SAVE_DIR = 'african_data_collector/storage/images'
CSV_FILE = 'african_data_collector/storage/meta_images.csv'

def main():

    collector = ImageCollector(ACCESS_KEY, SEARCH_TERMS, IMAGES_PER_TERM, SAVE_DIR, CSV_FILE)
    collector.collect_images()

    cleaner = DataCleaner(CSV_FILE)
    cleaner.remove_duplicates()
    cleaner.remove_missing_data()
    cleaner.save_cleaned_data()

    analyzer = DataAnalyzer(CSV_FILE)
    analyzer.analyze_categories()
    analyzer.analyze_description_length()

if __name__ == "__main__":
    main()

