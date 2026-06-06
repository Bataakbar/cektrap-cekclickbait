import os
import re
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model and tokenizer
MODEL_PATH = 'lstm_clickbait_model.keras'
TOKENIZER_PATH = 'tokenizer.pickle'

model = None
tokenizer = None

def load_nlp_assets():
    global model, tokenizer
    try:
        print("Loading LSTM model...")
        model = load_model(MODEL_PATH)
        print("Model loaded successfully!")
        
        print("Loading Tokenizer...")
        with open(TOKENIZER_PATH, 'rb') as handle:
            tokenizer = pickle.load(handle)
        print("Tokenizer loaded successfully!")
    except Exception as e:
        print(f"Error loading assets: {e}")

# Load assets on startup
load_nlp_assets()

def clean_text(text):
    # Standard cleanup like notebook
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_heuristics(text):
    # Extract features from the raw title
    exclamation_count = text.count('!')
    question_count = text.count('?')
    ellipsis_count = len(re.findall(r'\.\.\.', text))
    digit_count = len(re.findall(r'\d+', text))
    
    # Calculate capitalization ratio
    words = text.split()
    caps_word_count = sum(1 for w in words if w.isupper() and len(w) > 1)
    
    # Common clickbait word triggers in Indonesian
    clickbait_words = ['astaga', 'melongo', 'heboh', 'viral', 'terbongkar', 'rahasia', 'ternyata', 'bikin', 'netizen', 'mengejutkan', 'ngeri', 'waspada']
    matched_words = [w for w in clickbait_words if w in text.lower()]
    
    return {
        'exclamation_count': exclamation_count,
        'question_count': question_count,
        'ellipsis_count': ellipsis_count,
        'digit_count': digit_count,
        'caps_ratio': caps_word_count / len(words) if len(words) > 0 else 0,
        'has_clickbait_keywords': len(matched_words) > 0,
        'matched_keywords': matched_words
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None or tokenizer is None:
        return jsonify({
            'status': 'error',
            'message': 'Model NLP tidak termuat. Hubungi administrator.'
        }), 500
        
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Judul tidak boleh kosong.'
        }), 400
        
    title = data['title']
    
    # Extract heuristics
    heuristics = extract_heuristics(title)
    
    # Clean and predict
    cleaned = clean_text(title)
    seqs = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seqs, maxlen=30, padding='post', truncating='post')
    
    # Predict probability
    pred = model.predict(padded)
    probability = float(pred[0][0])
    
    # Determine classification label
    verdict = "CLICKBAIT" if probability >= 0.5 else "FAKTUAL"
    confidence = probability if verdict == "CLICKBAIT" else (1.0 - probability)
    
    return jsonify({
        'status': 'success',
        'title': title,
        'cleaned_title': cleaned,
        'probability': probability,
        'verdict': verdict,
        'confidence': round(confidence * 100, 2),
        'heuristics': heuristics
    })

@app.route('/api/report', methods=['POST'])
def report():
    # Mock endpoint to receive hoax reports
    data = request.form
    title = data.get('title')
    link = data.get('link', '')
    category = data.get('category', 'Lainnya')
    email = data.get('email', '')
    
    if not title:
        return jsonify({
            'status': 'error',
            'message': 'Judul berita wajib diisi.'
        }), 400
        
    # In a real app we might write this to a database, for now we return a success response with a unique ID
    import uuid
    report_id = f"CF-{uuid.uuid4().hex[:8].upper()}"
    
    return jsonify({
        'status': 'success',
        'message': 'Laporan berhasil terkirim. Terima kasih atas partisipasi Anda dalam melawan clickbait!',
        'report_id': report_id
    })

if __name__ == '__main__':
    # Run server on port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
