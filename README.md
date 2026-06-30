# 📰➡️🎬 Article to Reels

Turn any article URL into a ready-to-post Instagram Reel — automatically summarized, titled, voiced, and rendered into video.

**Live demo:** [https://article-to-reels.onrender.com](https://article-to-reels.onrender.com)

---

## ✨ Features

- **Article extraction** — paste any article URL and the app fetches and parses its content
- **AI summarization** — condenses the article into a short, reel-friendly summary
- **AI title generation** — generates a catchy title for the summary
- **Keyword extraction** — pulls out key topics/keywords from the summary
- **Multi-language translation** — translate the summary into your language of choice
- **Text-to-speech voiceover** — converts the summary into an audio voiceover
- **Automatic video creation** — combines the title, summary text, and voiceover into a short video, ready for Instagram Reels

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **NLP:** NLTK (sentence tokenization), custom summarization & keyword extraction modules
- **Frontend:** HTML, CSS
- **Deployment:** Render (Gunicorn WSGI server)

---

## 📂 Project Structure

```
article_to_reels/
├── app.py                   # Flask app entry point
├── build.sh                 # Build script (system dependencies, etc.)
├── procfile                  # Process file for deployment (gunicorn)
├── requirements.txt          # Python dependencies
├── runtime.txt                # Python runtime version
├── modules/
│   ├── fetch_article.py      # Article fetching & parsing
│   ├── summarizer.py         # Text summarization
│   ├── title_generator.py    # AI title generation
│   ├── translator.py         # Multi-language translation
│   ├── keyword_extractor.py  # Keyword extraction
│   ├── video_creator.py      # Video creation
│   └── voice_generator.py    # Text-to-speech voiceover
├── static/                   # Generated audio/video & static assets
├── templates/
│   └── index.html            # Main UI
└── assests/                   # Images / design assets
```

---

## 🚀 Getting Started Locally

### Prerequisites

- Python 3.x
- `ffmpeg` installed and available on your system PATH (required for video/audio processing)

### Installation

```bash
# Clone the repository
git clone https://github.com/Rajeswari-A-5/article_to_reels.git
cd article_to_reels

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

The app will be available at `http://localhost:5000`.

---

## 🌐 Deployment (Render)

This project is deployed on [Render](https://render.com) using Gunicorn.

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn app:app --bind 0.0.0.0:$PORT
```

---

## 📋 How to Use

1. Open the app in your browser
2. Paste the URL of the article you want to convert
3. Select your desired output language
4. Submit the form
5. The app will display the original title, AI-generated title, summary, translation, and provide an audio voiceover and a generated video — ready to download and post as a Reel

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/Rajeswari-A-5/article_to_reels/issues).

---

## 📄 License

This project currently has no license specified. Feel free to reach out to the author for usage permissions.

---

## 👤 Author

**Rajeswari A**
GitHub: [@Rajeswari-A-5](https://github.com/Rajeswari-A-5)
