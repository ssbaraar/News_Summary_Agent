import nltk
import os

def download_nltk_data():
    # Set the NLTK data path to a directory in your project
    nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
    os.environ['NLTK_DATA'] = nltk_data_path

    # Download required NLTK data
    nltk.download('punkt', quiet=True, download_dir=nltk_data_path)
    nltk.download('stopwords', quiet=True, download_dir=nltk_data_path)

if __name__ == "__main__":
    download_nltk_data()
    print("NLTK data downloaded successfully.")