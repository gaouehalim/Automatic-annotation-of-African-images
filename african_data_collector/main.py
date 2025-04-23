from data_collection import ImageCollector
from data_cleaning import DataCleaner
from data_analysis import DataAnalyzer
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

SEARCH_TERMS = [
    "african market",
    "african village",
    "african culture",
    "african music",
    "african dance",
    "african art",
    "african wildlife",
    "african landscape",
    "african festival",
    "african tradition",
    "african fashion",
    "african food",
    "african history",
    "african architecture",
    "african community",
    "african family",
    "african children",
    "african education",
    "african sports",
    "african religion",
    "african environment",
    "african health",
    "african photography",
    "african technology",
    "african travel",
    "burkina faso",
    "burundi",
    "cabo verde",
    "cameroun",
    "republic of the congo",
    "democratic republic of the congo",
    "djibouti",
    "egypte",
    "ethiopia",
    "gabon",
    "gambia",
    "ghana",
    "guinea",
    "guinea-bissau",
    "ivory coast",
    "benin",
    "kenya",
    "lesotho",
    "liberia",
    "libya",
    "madagascar",
    "malawi",
    "mali",
    "mauritania",
    "mauritius",
    "morocco",
    "mozambique",
    "namibia",
    "niger",
    "nigeria",
    "rwanda",
    "senegal",
    "seychelles",   
    "south africa",
    "south sudan",
    "sudan",
    "tanzania",
    "togo",
    "uganda",
    "zambia",
    "zimbabwe",
    ]


IMAGES_PER_TERM = 10


SAVE_DIR = 'african_data_collector/storage/images'
CSV_FILE = 'african_data_collector/storage/meta_images_final.csv'

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

