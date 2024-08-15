# Database Configuration
DATABASE_URL = "sqlite:///blockchain_intel.db"

# Data Acquisition Configuration
NEWS_SOURCES = [
    {"name": "GreenBiz", "url": "https://www.greenbiz.com/", "rss": "https://rss.app/feeds/PfSPW1PZmIDrjC8u.xml", "type": "both"},
    {"name": "Green Earth", "url": "https://www.green.earth", "rss": "https://rss.app/feeds/bovDvfqaIz2KoDdw.xml", "type": "both"},
    {"name": "Sustainable Brands", "url": "https://sustainablebrands.com/", "rss": "https://rss.app/feeds/qKjOEYXW4oEP6xYP.xml", "type": "both"},
    {"name": "Carbon Credits", "url": "https://carboncredits.com/", "rss": "https://rss.app/feeds/56HKOZAvi3Ym1tm7.xml", "type": "both"},
    {"name": "Triple Pundit", "url": "https://www.triplepundit.com/", "rss": "https://rss.app/feeds/uZLwiQhErv8b4yEK.xml", "type": "both"},
    {"name": "ESG Today", "url": "https://www.esgtoday.com/", "rss": "https://rss.app/feeds/K2enb0duBnv1BgXn.xml", "type": "both"},
    {"name": "CoinDesk", "url": "https://www.coindesk.com/", "rss": "https://rss.app/feeds/YqqGCKRoUgtzQxse.xml", "type": "both"},
    {"name": "Forbes", "url": "https://www.forbes.com/", "rss": "https://rss.app/feeds/AlOYwfMt50xeeAGX.xml", "type": "both"},
    {"name": "BusinessWire", "url": "https://www.businesswire.com/portal/site/home/news/", "type": "web"},
    {"name": "PRWeb", "url": "https://www.prweb.com/releases/news-releases-list/", "rss": "https://rss.app/feeds/4zjgvZfHGaKwST6D.xml", "type": "both"},
]

KEYWORD_RSS_FEEDS = [
    {"keyword": "Tokenization", "url": "https://rss.app/rss-feed?keyword=Tokenization&region=US&lang=en"},
    {"keyword": "DLT", "url": "https://rss.app/rss-feed?keyword=DLT&region=US&lang=en"},
    {"keyword": "RWA", "url": "https://rss.app/rss-feed?keyword=RWA&region=US&lang=en"},
    {"keyword": "Nature Based Credits", "url": "https://rss.app/rss-feed?keyword=Nature%20Based%20Credits&region=US&lang=en"},
    {"keyword": "Biodiversity", "url": "https://rss.app/rss-feed?keyword=Biodiversity&region=US&lang=en"},
]

OPENAI_API_KEY = "Your-api-key"
ALL_ARTICLES_FILE = "all_articles.json"
SCRAPED_DATA_FILE = "scraped_articles.json"
# Content Analysis Configuration
SUMMARY_LENGTH = 150  # Maximum length of the summary
KEYWORDS_PER_ARTICLE = 5  # Number of keywords to extract per article

# Scheduling
NORMAL_INTERVAL = 900  # 15 minutes in seconds
RETRY_INTERVAL = 300   # 5 minutes in seconds

# File Paths
SUMMARIZED_ARTICLES_FILE = "summarized_articles.json"
REPORT_OUTPUT_DIR = "reports"

# Logging
LOG_LEVEL = "INFO"

# # User Agent for web scraping (optional, but recommended)
# USER_AGENT = "YourProjectName/1.0 (your@email.com)"

# Request timeout for web scraping (in seconds)
REQUEST_TIMEOUT = 30

# Maximum number of retries for failed requests
MAX_RETRIES = 3

# Delay between retries (in seconds)
RETRY_DELAY = 5

# Rate limiting (requests per second)
RATE_LIMIT = 1

# Enable/Disable specific agents
ENABLE_DATA_ACQUISITION = True
ENABLE_CONTENT_ANALYSIS = True
ENABLE_REPORTING = True

# Database configuration
DB_ECHO = False  # Set to True for SQL query logging

# Content cleaning options
REMOVE_HTML_TAGS = True
REMOVE_EXTRA_WHITESPACE = True

# Article deduplication
ENABLE_DEDUPLICATION = True
SIMILARITY_THRESHOLD = 0.9  # Threshold for considering articles as duplicates (0.0 to 1.0)

# Error handling
MAX_ERRORS_BEFORE_ABORT = 10  # Maximum number of errors before aborting the entire process

# Performance tuning
BATCH_SIZE = 50  # Number of articles to process in a single batch

# # Proxy configuration (if needed)
# USE_PROXY = False
# PROXY_URL = "http://your-proxy-url:port"

# SSL verification (set to False only if absolutely necessary and you understand the risks)
VERIFY_SSL = True