# AI News Aggregation and Analysis System

## Overview
This project is a sophisticated multi-agent system designed to automate the process of gathering, analyzing, and summarizing news articles from various sources. The system employs three specialized agents working in concert to deliver comprehensive news analysis and reporting.

## Core Components

### 1. EnhancedDataAcquisitionAgent
- Fetches articles from configured news sources and RSS feeds
- Handles both web scraping and RSS feed parsing
- Implements intelligent rate limiting and error handling
- Stores raw article data for processing

### 2. EnhancedContentAnalysisAgent
- Processes raw articles using natural language processing (NLP)
- Leverages OpenAI's GPT-3.5 Turbo for advanced summarization
- Extracts key topics and themes
- Generates concise article summaries
- Performs keyword analysis and categorization

### 3. EnhancedReportingAgent
- Generates structured reports from analyzed content
- Maintains article archives
- Separates new and previously processed articles
- Creates organized summaries for easy consumption

## Technical Requirements

### Dependencies
```
nltk==3.8.1
openai==1.3.0
loguru==0.7.2
python-dotenv==1.0.0
requests==2.31.0
beautifulsoup4==4.12.2
feedparser==6.0.10
```

### System Requirements
- Python 3.8+
- SQLite3
- 2GB+ RAM recommended
- Internet connection for API access

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   Create a `.env` file in the root directory with the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Configuration

The system is highly configurable through the `utils/config.py` file:

### News Sources
- Configurable list of news sources and RSS feeds
- Support for both web scraping and RSS parsing
- Custom keyword-based RSS feeds

### Processing Parameters
- Adjustable summary length
- Configurable number of keywords per article
- Customizable update intervals
- Flexible retry mechanisms

### Output Settings
- Configurable report directory
- Multiple output formats
- Customizable logging levels

## Usage

1. **Start the system**:
   ```sh
   python main.py
   ```

2. **Monitor Progress**:
   The system creates three log files:
   - `data_acquisition.log`: Tracks article fetching
   - `content_analysis.log`: Monitors processing
   - `reporting.log`: Records report generation

## Data Flow

1. **Acquisition Phase**
   - Fetches articles from configured sources
   - Validates and deduplicates content
   - Stores raw data in SQLite database

2. **Analysis Phase**
   - Processes raw content using NLP
   - Generates summaries using OpenAI
   - Extracts keywords and themes
   - Categorizes content

3. **Reporting Phase**
   - Generates structured reports
   - Archives processed articles
   - Creates searchable indexes

## File Structure
```
project/
├── agents/
│   ├── __init__.py
│   ├── data_acquisition_agent.py
│   ├── content_analysis_agent.py
│   └── reporting_agent.py
├── utils/
│   ├── __init__.py
│   └── config.py
├── data/
│   └── articles.db
├── reports/
├── .env
├── main.py
└── requirements.txt
```

## Logging

The system implements comprehensive logging using Loguru:
- Rotation-based log files
- Configurable log levels
- Detailed error tracking
- Performance metrics

## Error Handling

- Robust retry mechanisms for failed requests
- Graceful degradation for API limits
- Comprehensive error logging
- Data validation at each step

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - See LICENSE file for details