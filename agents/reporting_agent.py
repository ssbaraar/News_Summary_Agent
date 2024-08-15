import json
import os
from datetime import datetime
from loguru import logger
from utils.config import REPORT_OUTPUT_DIR, SUMMARIZED_ARTICLES_FILE

logger.add("reporting.log", rotation="500 MB")

class EnhancedReportingAgent:
    def __init__(self):
        self.last_report_time = self.get_last_report_time()

    def run(self):
        logger.info("Starting report generation...")
        self.generate_new_articles_report()
        logger.info("Report generation completed.")

    def generate_new_articles_report(self):
        all_articles = self.get_all_articles()
        new_articles, old_articles = self.separate_new_and_old_articles(all_articles)

        report = {
            "report_time": datetime.now().isoformat(),
            "total_articles": len(all_articles),
            "new_articles_count": len(new_articles),
            "new_articles": self.format_articles(new_articles),
            "old_articles": self.format_articles(old_articles)
        }

        self.save_report(report, "articles_report")
        self.update_last_report_time()

    def get_all_articles(self):
        try:
            with open(SUMMARIZED_ARTICLES_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Summarized articles file not found: {SUMMARIZED_ARTICLES_FILE}")
            return []
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from file: {SUMMARIZED_ARTICLES_FILE}")
            return []

    def separate_new_and_old_articles(self, articles):
        new_articles = []
        old_articles = []
        for article in articles:
            if datetime.fromisoformat(article['published_date']) > self.last_report_time:
                new_articles.append(article)
            else:
                old_articles.append(article)
        return new_articles, old_articles

    def format_articles(self, articles):
        return [
            {
                "title": article['title'],
                "url": article['url'],
                "source": article['source'],
                "published_date": article['published_date'],
                "summary": article['summary'],
                "keywords": article['keywords']
            }
            for article in articles
        ]

    def save_report(self, report, report_type):
        if not os.path.exists(REPORT_OUTPUT_DIR):
            os.makedirs(REPORT_OUTPUT_DIR)

        filename = f"{report_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(REPORT_OUTPUT_DIR, filename)

        try:
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Saved {report_type} to {filepath}")
        except IOError as e:
            logger.error(f"Error saving report to {filepath}: {str(e)}")

    def get_last_report_time(self):
        last_report_file = os.path.join(REPORT_OUTPUT_DIR, 'last_report_time.txt')
        try:
            with open(last_report_file, 'r') as f:
                return datetime.fromisoformat(f.read().strip())
        except FileNotFoundError:
            logger.warning("Last report time file not found. Using minimum datetime.")
            return datetime.min
        except ValueError:
            logger.error("Error parsing last report time. Using minimum datetime.")
            return datetime.min

    def update_last_report_time(self):
        last_report_file = os.path.join(REPORT_OUTPUT_DIR, 'last_report_time.txt')
        try:
            with open(last_report_file, 'w') as f:
                f.write(datetime.now().isoformat())
        except IOError as e:
            logger.error(f"Error updating last report time: {str(e)}")

    def initialize(self):
        if not os.path.exists(REPORT_OUTPUT_DIR):
            os.makedirs(REPORT_OUTPUT_DIR)
        logger.info("Enhanced Reporting Agent initialized.")

    def cleanup(self):
        logger.info("Enhanced Reporting Agent cleanup completed.")

if __name__ == "__main__":
    agent = EnhancedReportingAgent()
    agent.initialize()
    agent.run()
    agent.cleanup()