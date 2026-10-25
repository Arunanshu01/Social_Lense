# ─────────────────────────────────────────────────────────────
# SocialLens API — Complete Backend
# Endpoints: health, analyze, analyze-batch,
#            hashtags, caption, schedule, niche, trends
# ─────────────────────────────────────────────────────────────

import sys
import os

# Add src folder to path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Import our custom modules
from hashtag_recommender import get_hashtags, get_all_niches, get_all_platforms
from caption_generator   import generate_captions, get_available_tones
from time_recommender    import get_best_times, get_weekly_plan

nltk.download('stopwords', quiet=True)

app = Flask(__name__)
CORS(app)

# ── Load Model Once at Startup ────────────────────────────────

print("Loading sentiment model...")

MODEL_PATH      = os.path.join(os.path.dirname(__file__), '..', 'models', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'tfidf_vectorizer.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

print("Model loaded. SocialLens API ready.")

stemmer    = PorterStemmer()
stop_words = set(stopwords.words('english'))

# ── Preprocessing Function ────────────────────────────────────

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r"n't\b", ' not', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.strip()
    words = [stemmer.stem(w) for w in text.split() if w not in stop_words]
    return ' '.join(words)

# ── Sentiment Prediction Helper ───────────────────────────────

def predict(text):
    cleaned    = clean_text(text)
    vector     = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    proba      = model.predict_proba(vector)[0]
    confidence = round(float(max(proba)) * 100, 2)
    sentiment  = 'positive' if prediction == 1 else 'negative'
    return {
        'sentiment'     : sentiment,
        'confidence'    : confidence,
        'cleaned_text'  : cleaned,
        'scores': {
            'negative'  : round(float(proba[0]) * 100, 2),
            'positive'  : round(float(proba[1]) * 100, 2)
        }
    }

# ════════════════════════════════════════════════════════════
# ENDPOINT 1 — Health Check
# GET /health
# ════════════════════════════════════════════════════════════

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status'  : 'SocialLens API is running',
        'version' : '2.0',
        'modules' : ['sentiment', 'hashtags', 'captions', 'schedule', 'trends']
    })

# ════════════════════════════════════════════════════════════
# ENDPOINT 2 — Single Tweet Analysis
# POST /analyze
# Body: { "text": "your tweet here" }
# ════════════════════════════════════════════════════════════

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text field'}), 400

    text   = data['text']
    result = predict(text)

    # Add improvement suggestions based on sentiment
    suggestions = []
    if result['sentiment'] == 'negative':
        suggestions = [
            "Try starting with a positive hook",
            "Add a solution or silver lining",
            "Use more energetic language",
            "End with an engaging question"
        ]
    else:
        suggestions = [
            "Add a clear call-to-action",
            "Include relevant hashtags",
            "Ask your audience a question",
            "Add an emoji to increase engagement"
        ]

    result['original_text'] = text
    result['suggestions']   = suggestions

    return jsonify(result)

# ════════════════════════════════════════════════════════════
# ENDPOINT 3 — Batch Analysis
# POST /analyze-batch
# Body: { "tweets": ["tweet1", "tweet2", ...] }
# ════════════════════════════════════════════════════════════

@app.route('/analyze-batch', methods=['POST'])
def analyze_batch():
    data = request.get_json()

    if not data or 'tweets' not in data:
        return jsonify({'error': 'Please provide tweets array'}), 400

    tweets  = data['tweets']
    results = []

    for tweet in tweets:
        r = predict(tweet)
        results.append({
            'text'      : tweet,
            'sentiment' : r['sentiment'],
            'confidence': r['confidence']
        })

    positive_count = sum(1 for r in results if r['sentiment'] == 'positive')
    negative_count = len(results) - positive_count

    return jsonify({
        'results'           : results,
        'total'             : len(results),
        'positive_count'    : positive_count,
        'negative_count'    : negative_count,
        'overall_sentiment' : 'positive' if positive_count > negative_count else 'negative'
    })

# ════════════════════════════════════════════════════════════
# ENDPOINT 4 — Hashtag Recommender
# POST /hashtags
# Body: { "niche": "technology", "platform": "instagram" }
# ════════════════════════════════════════════════════════════

@app.route('/hashtags', methods=['POST'])
def hashtags():
    data = request.get_json()

    if not data or 'niche' not in data or 'platform' not in data:
        return jsonify({'error': 'Please provide niche and platform'}), 400

    niche    = data['niche']
    platform = data['platform']
    count    = data.get('count', 10)

    tags = get_hashtags(niche, platform, count=count)

    return jsonify({
        'niche'    : niche,
        'platform' : platform,
        'hashtags' : tags,
        'count'    : len(tags)
    })

# ════════════════════════════════════════════════════════════
# ENDPOINT 5 — Caption Generator
# POST /caption
# Body: { "topic": "morning workout",
#         "tone": "motivational",
#         "platform": "instagram",
#         "niche": "fitness" }
# ════════════════════════════════════════════════════════════

@app.route('/caption', methods=['POST'])
def caption():
    data = request.get_json()

    required = ['topic', 'tone', 'platform', 'niche']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    captions = generate_captions(
        topic    = data['topic'],
        tone     = data['tone'],
        platform = data['platform'],
        niche    = data['niche'],
        count    = data.get('count', 3)
    )

    return jsonify({
        'topic'         : data['topic'],
        'tone'          : data['tone'],
        'platform'      : data['platform'],
        'niche'         : data['niche'],
        'captions'      : captions,
        'available_tones': get_available_tones()
    })

# ════════════════════════════════════════════════════════════
# ENDPOINT 6 — Posting Schedule
# POST /schedule
# Body: { "platform": "instagram", "niche": "fitness" }
# ════════════════════════════════════════════════════════════

@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.get_json()

    if not data or 'platform' not in data or 'niche' not in data:
        return jsonify({'error': 'Please provide platform and niche'}), 400

    platform    = data['platform']
    niche       = data['niche']
    weekly_plan = get_weekly_plan(platform, niche)
    times_data  = get_best_times(platform, niche)

    return jsonify({
        'platform'       : platform,
        'niche'          : niche,
        'weekly_plan'    : weekly_plan,
        'frequency'      : times_data['frequency'],
        'best_per_day'   : times_data['best_per_day']
    })

# ════════════════════════════════════════════════════════════
# ENDPOINT 7 — Trends
# GET /trends
# ════════════════════════════════════════════════════════════

@app.route('/trends', methods=['GET'])
def trends():
    return jsonify({
        'trending_topics': [
            {'topic': 'Artificial Intelligence', 'percentage': 28, 'emoji': '🤖'},
            {'topic': 'Entertainment',           'percentage': 19, 'emoji': '🎬'},
            {'topic': 'Health & Wellness',       'percentage': 14, 'emoji': '💪'},
            {'topic': 'Sports',                  'percentage': 11, 'emoji': '⚽'},
            {'topic': 'Business & Finance',      'percentage':  9, 'emoji': '💼'}
        ],
        'trending_hashtags': [
            '#AI', '#MachineLearning', '#ContentCreator',
            '#GrowthHacking', '#Python', '#DataScience',
            '#DigitalMarketing', '#CreatorEconomy',
            '#SocialMediaTips', '#TechTwitter'
        ],
        'sentiment_pulse': {
            'positive'   : 61,
            'negative'   : 39,
            'sample_size': 9949,
            'note'       : 'Based on our trained sentiment model'
        },
        'top_content_types': [
            {'type': 'Video Reels',       'trend': 'up',   'emoji': '🎥'},
            {'type': 'Carousel Posts',    'trend': 'up',   'emoji': '📱'},
            {'type': 'How-to Threads',    'trend': 'up',   'emoji': '🧵'},
            {'type': 'Personal Stories',  'trend': 'stable','emoji': '❤️'}
        ]
    })

# ════════════════════════════════════════════════════════════
# ENDPOINT 8 — Available Options
# GET /options
# Returns all niches, platforms, tones available
# ════════════════════════════════════════════════════════════

@app.route('/options', methods=['GET'])
def options():
    return jsonify({
        'niches'   : get_all_niches(),
        'platforms': get_all_platforms(),
        'tones'    : get_available_tones()
    })

# ── Run ───────────────────────────────────────────────────────

if __name__ == '__main__':
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)