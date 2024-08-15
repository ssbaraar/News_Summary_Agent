import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from loguru import logger
import openai
from typing import List, Dict
import os

# Assuming these are defined in your config file
from utils.config import (
    KEYWORDS_PER_ARTICLE,
    SUMMARY_LENGTH,
    SUMMARIZED_ARTICLES_FILE,
    SCRAPED_DATA_FILE,
    ALL_ARTICLES_FILE,
    OPENAI_API_KEY
)

class EnhancedContentAnalysisAgent:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.summarized_articles = []
        openai.api_key = OPENAI_API_KEY

    def initialize(self):
        logger.info("Initializing Enhanced Content Analysis Agent...")
        logger.info("Enhanced Content Analysis Agent initialized.")

    def run(self):
        logger.info("Starting content analysis...")
        existing_articles = self.load_articles(ALL_ARTICLES_FILE)
        newly_scraped_articles = self.load_articles(SCRAPED_DATA_FILE)

        all_articles = existing_articles + newly_scraped_articles

        for article in all_articles:
            self.process_article(article)

        self.save_summarized_articles()
        logger.info(f"Completed content analysis for {len(all_articles)} articles.")

    def load_articles(self, file_path: str) -> List[Dict]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return []
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from file: {file_path}")
            return []

    def process_article(self, article: Dict):
        try:
            keywords = self.extract_keywords(article['content'])
            summary = self.generate_summary(article['content'])

            self.summarized_articles.append({
                "id": article['id'],
                "title": article['title'],
                "url": article['url'],
                "source": article['source'],
                "published_date": article['published_date'],
                "keywords": keywords,
                "summary": summary
            })

            logger.info(f"Processed article: {article['title']}")
        except KeyError as e:
            logger.error(f"Missing key in article data: {e}")
        except Exception as e:
            logger.error(f"Error processing article {article.get('id', 'Unknown')}: {str(e)}")

    def extract_keywords(self, text: str) -> List[str]:
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum() and word not in self.stop_words]
        freq_dist = FreqDist(words)
        return [word for word, _ in freq_dist.most_common(KEYWORDS_PER_ARTICLE)]

    def generate_summary(self, text: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                    {"role": "user", "content": f"Please summarize the following text in about {SUMMARY_LENGTH} characters:\n\n{text}"}
                ],
                max_tokens=SUMMARY_LENGTH // 4,  # Approximate token count
                n=1,
                stop=None,
                temperature=0.7,
            )
            summary = response.choices[0].message['content'].strip()
            return summary[:SUMMARY_LENGTH] + "..." if len(summary) > SUMMARY_LENGTH else summary
        except Exception as e:
            logger.error(f"Error generating summary using OpenAI: {str(e)}")
            return "Summary generation failed."

    def save_summarized_articles(self):
        if self.summarized_articles:
            with open(SUMMARIZED_ARTICLES_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.summarized_articles, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved {len(self.summarized_articles)} summarized articles to {SUMMARIZED_ARTICLES_FILE}")
        else:
            logger.warning("No articles were summarized in this run.")

    def cleanup(self):
        logger.info("Enhanced Content Analysis Agent cleanup completed.")

def main():
    try:
        agent = EnhancedContentAnalysisAgent()
        agent.initialize()
        agent.run()
        agent.cleanup()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()