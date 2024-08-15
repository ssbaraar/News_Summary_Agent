from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words

# from database.models import Session


def __init__(self):
    self.session = Session()
    self.summarizer = LsaSummarizer(Stemmer('english'))
    self.summarizer.stop_words = get_stop_words('english')
    self.summarized_articles = []
    # Remove the stopwords initialization from here