import os
import json
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# NewsAPI Configuration
API_KEY = os.getenv('NEWS_API_KEY')
BASE_URL = 'https://newsapi.org/v2/top-headlines'
SAVED_ARTICLES_FILE = 'saved_articles.json'

def load_saved_articles():
    """Load saved articles from JSON file."""
    try:
        with open(SAVED_ARTICLES_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_articles_to_file(articles):
    """Save articles to JSON file."""
    with open(SAVED_ARTICLES_FILE, 'w') as f:
        json.dump(articles, f, indent=4)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/get_news')
def get_news():
    """Fetch news articles based on query parameters."""
    # Get query parameters
    category = request.args.get('category', '')
    keyword = request.args.get('keyword', '')
    source = request.args.get('source', '')

    # Prepare parameters for NewsAPI
    params = {
        'apiKey': API_KEY,
        'language': 'en'
    }

    # Add optional parameters
    if category:
        params['category'] = category
    if keyword:
        params['q'] = keyword
    if source:
        params['sources'] = source

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        news_data = response.json()
        return jsonify(news_data['articles'])
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save_article', methods=['POST'])
def save_article():
    """Save an article to saved_articles.json."""
    article = request.json
    saved_articles = load_saved_articles()
    
    # Check if article already exists
    if not any(a['url'] == article['url'] for a in saved_articles):
        saved_articles.append(article)
        save_articles_to_file(saved_articles)
        return jsonify({'status': 'success', 'message': 'Article saved'})
    
    return jsonify({'status': 'error', 'message': 'Article already saved'})

@app.route('/saved_articles')
def saved_articles():
    """Render saved articles page."""
    saved_articles = load_saved_articles()
    return render_template('saved_articles.html', articles=saved_articles)

@app.route('/remove_article', methods=['POST'])
def remove_article():
    """Remove an article from saved_articles.json."""
    url = request.json.get('url')
    saved_articles = load_saved_articles()
    
    # Remove article with matching URL
    saved_articles = [a for a in saved_articles if a['url'] != url]
    save_articles_to_file(saved_articles)
    
    return jsonify({'status': 'success', 'message': 'Article removed'})

if __name__ == '__main__':
    app.run(debug=True)
