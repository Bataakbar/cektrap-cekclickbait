import os
import re
import torch
from flask import Flask, request, jsonify, render_template
from transformers import BertForSequenceClassification, AutoTokenizer

app = Flask(__name__)

# Load model and tokenizer
MODEL_DIR = './'

model = None
tokenizer = None

def load_nlp_assets():
    global model, tokenizer
    try:
        print("Loading BERT Tokenizer from local files...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        print("Tokenizer loaded successfully!")
        
        print("Loading BERT model from local files...")
        model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
        model.eval()
        print("BERT model loaded successfully!")
    except Exception as e:
        print(f"Error loading assets: {e}")

# Load assets on startup
load_nlp_assets()

def clean_text(text):
    # Bersihkan URL dan spasi berlebih
    # Sengaja TIDAK hapus ? dan ! karena itu sinyal kuat clickbait
    text = str(text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # hapus URL
    text = re.sub(r'\s+', ' ', text).strip()              # rapikan spasi
    return text

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
    
    # Clean and predict
    cleaned = clean_text(title)
    inputs = tokenizer(cleaned, return_tensors="pt", padding="max_length", truncation=True, max_length=64)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=-1)
        
    # Class 1 is CLICKBAIT, Class 0 is FAKTUAL
    probability = float(probs[0][1].item())
    
    # Determine classification label
    verdict = "CLICKBAIT" if probability >= 0.4 else "FAKTUAL"
    confidence = probability if verdict == "CLICKBAIT" else (1.0 - probability)

    
    return jsonify({
        'status': 'success',
        'title': title,
        'cleaned_title': cleaned,
        'probability': probability,
        'verdict': verdict,
        'confidence': round(confidence * 100, 2)
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
    # Run server on port 5000 or dynamic PORT from env (required by Railway)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
