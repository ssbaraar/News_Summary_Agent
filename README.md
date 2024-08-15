# AI News Aggregation and Analysis System

This project is a multi-agent system designed to automate the process of subscribing to news sites, fetching newly published articles, and summarizing them. The system is composed of three main agents: `EnhancedDataAcquisitionAgent`, `EnhancedContentAnalysisAgent`, and `EnhancedReportingAgent`.

## Features

- **Data Acquisition**: Fetches articles from various news sources and RSS feeds.
- **Content Analysis**: Extracts keywords and generates summaries for new articles using natural language processing techniques and OpenAI's GPT-3.5 Turbo model.
- **Reporting**: Saves summarized articles and generates reports, separating new articles from old ones.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. **Set up a virtual environment (optional but recommended)**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the required dependencies**:
   pip install -r requirements.txt

   Environment Setup
Create a .env file in the root directory of the project.

Add your OpenAI API key to the .env file:

OPENAI_API_KEY=your_openai_api_key

Running the Project
Run the main script:

python main.py

Monitoring
Monitor the logs:

The agents will log their activities to data_acquisition.log, content_analysis.log, and reporting.log files respectively.

Configuration
NEWS_SOURCES: List of news sources and RSS feeds to fetch articles from.
KEYWORD_RSS_FEEDS: List of RSS feeds based on specific keywords.
SUMMARY_LENGTH: Length of the summary to be generated for each article.
REPORT_OUTPUT_DIR: Directory where reports will be saved.