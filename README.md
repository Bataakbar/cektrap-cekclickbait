# ClickTrap — Pendeteksi Clickbait Bahasa Indonesia (LSTM)

**ClickTrap** adalah platform berbasis web premium yang dirancang untuk mendeteksi *clickbait* (umpan klik) pada judul berita berbahasa Indonesia. Platform ini mengombinasikan kekuatan model Deep Learning **Bidirectional LSTM** dengan analisis heuristik linguistik untuk memberikan penilaian secara transparan dan akurat.

---

## 📊 Sumber Dataset

Model LSTM ini dilatih menggunakan dataset **ClickID** (sekitar 15.000 judul berita bahasa Indonesia yang diklasifikasi secara manual) yang diperoleh dari Kaggle:
👉 **[ClickID Dataset di Kaggle](https://www.kaggle.com/datasets/andikawilliam/clickid)** oleh Andika William.

---

## ✨ Fitur Utama

1. **AI Clickbait Detector**: Menganalisis kalimat/judul berita secara instan menggunakan model Deep Learning LSTM yang dilatih secara khusus untuk memahami semantik judul bahasa Indonesia.
2. **Linguistic Heuristic Analyzer**: Mendeteksi pola kemenarikan emosional, huruf kapital berlebih, tanda baca berlebih, dan mencocokkan kosakata pemicu clickbait (*viral, terbongkar, astaga*, dll.).
3. **Direktori Clickbait**: Kumpulan contoh judul berita clickbait dari dataset ClickID lokal lengkap dengan kategori, tanggal rilis, dan tautan klarifikasinya.
4. **Metodologi Transparan**: Alur deteksi terperinci yang mencakup *parsing* linguistik, pencocokan pola, skor emosional, dan rekomendasi judul wajar.
5. **Ensiklopedi Pola**: Edukasi mendalam mengenai 6 pola clickbait utama yang sering ditemui (seperti *Curiosity Gap, Fear Mongering, Listicle Bait*, dsb.) beserta contoh riilnya.
6. **Citizen Report**: Formulir pelaporan berita clickbait atau mencurigakan oleh masyarakat.

---

## 🛠️ Spesifikasi Teknologi

*   **Backend**: Flask (Python 3), TensorFlow/Keras (untuk inferensi model LSTM), Pickle (untuk load tokenizer nlp).
*   **Frontend**: HTML5, CSS3 murni (Premium Light Mode layout, animasi visual kursor/tombol *Click Spark* pada judul beranda, status bar iPhone XR mockup screen), Vanilla JS.

---

## 🚀 Cara Menjalankan Proyek

### 1. Prasyarat
Pastikan Anda sudah menginstal Python (versi 3.9 - 3.11 direkomendasikan).

### 2. Instalasi Dependensi
Instal pustaka-pustaka yang diperlukan menggunakan pip:
```bash
pip install flask tensorflow numpy requests
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
