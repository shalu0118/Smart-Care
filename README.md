# Smart Care — Multilingual Symptom Mapper and Drug Analyzer

An AI-powered healthcare platform that helps users understand prescriptions, 
check medicine safety, and get preliminary symptom guidance — in multiple 
languages, without needing medical expertise.

## Features (In Progress)

- ✅ User health profile management (registration, login, secure password hashing)
- ✅ REST API backend with Flask + SQLite
- 🔜 Prescription OCR scanning and translation
- 🔜 Drug interaction & allergy safety checks (openFDA)
- 🔜 AI symptom classification (TF-IDF + Naive Bayes)
- 🔜 Multilingual voice/text symptom checker
- 🔜 Smartwatch health monitoring integration

## Tech Stack

**Backend:** Python, Flask, Flask-SQLAlchemy, SQLite  
**ML/NLP:** scikit-learn (TF-IDF + Naive Bayes), NLTK  
**Auth:** Werkzeug password hashing  
**Frontend:** Flutter (planned)

## Getting Started

```bash
cd Smart_Care_Backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python app.py
```

Server runs at `http://127.0.0.1:5000`

### API Endpoints (Module 1)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/api/user/profile` | Create user profile |
| GET | `/api/user/profile/<id>` | Get user profile |
| POST | `/api/login` | User login |

## Status

🚧 Under active development — final year student project.
