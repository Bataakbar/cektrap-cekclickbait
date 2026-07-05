# ClickTrap — Pendeteksi Clickbait Bahasa Indonesia (BERT)

**ClickTrap** adalah platform berbasis web premium yang dirancang untuk mendeteksi *clickbait* (umpan klik) pada judul berita berbahasa Indonesia. Platform ini mengombinasikan kekuatan model Transformer **BERT** (Bidirectional Encoder Representations from Transformers) dengan analisis heuristik linguistik untuk memberikan penilaian secara transparan dan akurat.

---

## 📊 Sumber Dataset & Model

Model BERT ini dilatih menggunakan dataset **ClickID** (sekitar 15.000 judul berita bahasa Indonesia yang diklasifikasi secara manual) yang diperoleh dari Kaggle:
👉 **[ClickID Dataset di Kaggle](https://www.kaggle.com/datasets/andikawilliam/clickid)** oleh Andika William.

Arsitektur model BERT memanfaatkan mekanisme *self-attention* dua arah secara penuh untuk menangkap konteks semantik judul berita dengan akurasi yang jauh lebih tinggi dan stabil dibanding model sekuensial tradisional.

---

## ✨ Fitur Utama

1. **AI Clickbait Detector**: Menganalisis kalimat/judul berita secara instan menggunakan model Deep Learning BERT yang dikonfigurasi dan dilatih secara khusus untuk memahami semantik bahasa Indonesia.
2. **Linguistic Heuristic Analyzer**: Mendeteksi pola kemenarikan emosional, huruf kapital berlebih, tanda baca berlebih, dan mencocokkan kosakata pemicu clickbait (*viral, terbongkar, astaga*, dll.).
3. **Direktori Clickbait**: Kumpulan contoh judul berita clickbait dari dataset ClickID lokal lengkap dengan kategori, tanggal rilis, dan tautan klarifikasinya.
4. **Metodologi Transparan**: Alur deteksi terperinci yang mencakup *parsing* linguistik, pencocokan pola, skor emosional, dan rekomendasi judul wajar.
5. **Ensiklopedi Pola**: Edukasi mendalam mengenai 6 pola clickbait utama yang sering ditemui (seperti *Curiosity Gap, Fear Mongering, Listicle Bait*, dsb.) beserta contoh riilnya.
6. **Citizen Report**: Formulir pelaporan berita clickbait atau mencurigakan oleh masyarakat.

---

## 🛠️ Spesifikasi Teknologi

*   **Backend**: Flask (Python 3), PyTorch & Hugging Face Transformers (untuk inferensi model BERT), Safetensors (untuk load weights model).
*   **Frontend**: HTML5, CSS3 murni (Premium Light Mode layout, status bar iPhone XR mockup screen), Vanilla JS.

---

## 🚀 Cara Menjalankan Proyek

### 1. Prasyarat
Pastikan Anda sudah menginstal Python (versi 3.9 - 3.11 direkomendasikan).

### 2. Instalasi Dependensi
Instal pustaka-pustaka yang diperlukan menggunakan pip:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
Jalankan server lokal Flask:
```bash
python app.py
```

### 4. Akses Web
Buka browser Anda dan akses tautan berikut:
```text
http://127.0.0.1:5000/
```
