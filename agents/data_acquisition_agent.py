import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database.models import Session, Article
from utils.config import NEWS_SOURCES, KEYWORD_RSS_FEEDS, ALL_ARTICLES_FILE
from loguru import logger
import sys
import time
from sqlalchemy.exc import SQLAlchemyError
from requests.exceptions import RequestException
import json
import os

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("data_acquisition.log", rotation="500 MB")

class DataAcquisitionAgent:
    def __init__(self):
        self.session = Session()
        self.all_articles = self.load_existing_articles()

    def load_existing_articles(self):
        if os.path.exists(ALL_ARTICLES_FILE):
            try:
                with open(ALL_ARTICLES_FILE, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.error(f"Error decoding JSON from {ALL_ARTICLES_FILE}. Starting with empty list.")
                return []
        else:
            logger.info(f"{ALL_ARTICLES_FILE} not found. Starting with empty list.")
            return []

    def run(self):
        start_time = time.time()
        new_article_count = self.fetch_and_store_articles()
        self.save_all_articles()
        end_time = time.time()
        logger.info(f"Run completed. Fetched {new_article_count} new articles in {end_time - start_time:.2f} seconds.")

    def fetch_and_store_articles(self):
        new_article_count = 0
        for source in NEWS_SOURCES + KEYWORD_RSS_FEEDS:
            source_name = source.get('name', source.get('keyword', 'Unknown'))
            logger.info(f"Fetching articles for {source_name}")
            try:
                if source.get('type') in ['rss', 'both'] or 'keyword' in source:
                    new_article_count += self.fetch_from_rss(source)
                if source.get('type') in ['web', 'both']:
                    new_article_count += self.fetch_from_web(source)
                time.sleep(2)  # Add a 2-second delay between requests
            except Exception as e:
                logger.error(f"Error fetching from {source_name}: {str(e)}")
        return new_article_count

    def fetch_from_rss(self, source):
        count = 0
        feed_url = source.get('rss', source['url'])
        try:
            feed = feedparser.parse(feed_url)
            logger.info(f"Fetched {len(feed.entries)} entries from {feed_url}")
            for entry in feed.entries:
                article = self.create_article_from_rss(entry, source.get('name', source.get('keyword', 'Unknown')))
                if not self.article_exists(article.url):
                    self.session.add(article)
                    self.all_articles.append(self.article_to_dict(article))
                    count += 1
            self.session.commit()
        except Exception as e:
            logger.error(f"Error processing RSS feed {feed_url}: {str(e)}")
            self.session.rollback()
        logger.info(f"Added {count} new articles from {feed_url}")
        return count

    def fetch_from_web(self, source):
        count = 0
        try:
            response = requests.get(source['url'], timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = self.extract_articles_from_soup(soup, source)
            logger.info(f"Extracted {len(articles)} articles from {source['url']}")
            for article_data in articles:
                article = self.create_article_from_web(article_data, source['name'])
                if not self.article_exists(article.url):
                    self.session.add(article)
                    self.all_articles.append(self.article_to_dict(article))
                    count += 1
            self.session.commit()
        except RequestException as e:
            logger.error(f"Network error fetching {source['url']}: {str(e)}")
        except Exception as e:
            logger.error(f"Error processing web source {source['url']}: {str(e)}")
            self.session.rollback()
        logger.info(f"Added {count} new articles from {source['url']}")
        return count

    def extract_articles_from_soup(self, soup, source):
        articles = []
        for article in soup.find_all(['article', 'div', 'li'], class_=['post', 'article', 'news-item']):
            title_tag = article.find(['h2', 'h3', 'h4', 'a'], class_=['title', 'headline'])
            link_tag = article.find('a', href=True)
            if title_tag and link_tag:
                articles.append({
                    'title': title_tag.text.strip(),
                    'url': link_tag['href'] if link_tag['href'].startswith('http') else source['url'] + link_tag['href'],
                    'summary': article.find('p', class_=['summary', 'excerpt']).text.strip() if article.find('p', class_=['summary', 'excerpt']) else ''
                })
        return articles

    def article_exists(self, url):
        return any(article['url'] == url for article in self.all_articles)

    def create_article_from_rss(self, entry, source_name):
        return Article(
            title=entry.title,
            url=entry.link,
            source=source_name,
            published_date=self.parse_date(entry),
            content=entry.get('summary', '')
        )

    def create_article_from_web(self, article, source_name):
        return Article(
            title=article['title'],
            url=article['url'],
            source=source_name,
            published_date=datetime.now(),
            content=article['summary']
        )

    def parse_date(self, entry):
        for date_field in ['published', 'updated', 'created']:
            if date_field in entry:
                try:
                    return datetime(*entry[f"{date_field}_parsed"][:6])
                except:
                    pass
        return datetime.now()

    def article_to_dict(self, article):
        return {
            'id': article.id,
            'title': article.title,
            'url': article.url,
            'source': article.source,
            'published_date': article.published_date.isoformat(),
            'content': article.content
        }

    def save_all_articles(self):
        with open(ALL_ARTICLES_FILE, 'w') as f:
            json.dump(self.all_articles, f, indent=2)
        logger.info(f"Saved {len(self.all_articles)} articles to {ALL_ARTICLES_FILE}")

    def cleanup(self):
        self.session.close()

    def initialize(self):
        logger.info("Data Acquisition Agent initialized.")

if __name__ == "__main__":
    agent = DataAcquisitionAgent()
    agent.initialize()
    agent.run()
    agent.cleanup()