# 🚀 Vehicle Price Estimator – Deployment Guide

This document explains how the Vehicle Price Estimator ML application
is deployed in production using **Render.com**.

---

## 🔧 Tech Stack
- Python 3.12
- Flask (Backend)
- Scikit-Learn (ML Pipeline)
- Pandas & NumPy (Data Processing)
- Gunicorn (Production WSGI Server)
- Render.com (Cloud Hosting)

---

## 📦 Project Structure
\`\`\`text
.
├── app.py
├── model.pkl
├── requirements.txt
├── render.yaml
├── templates/
├── static/
└── DEPLOYMENT.md
\`\`\`

---

## 🤖 Model Details
- Trained using a Scikit-Learn pipeline
- Preprocessing handled internally (encoding + scaling)
- Serialized using \`joblib\`
- Loaded safely at runtime with validation & fallback checks

**Model Version:** v1.0

---

## ☁️ Render Deployment

### Build Settings

**Build Command**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**Start Command**
\`\`\`bash
gunicorn app:app
\`\`\`

### ❤️ Health Check
The application exposes a health endpoint:
\`\`\`text
/healthz
\`\`\`
Used by Render to verify service availability.

### 🔄 Auto Deployment
- Connected to GitHub (main branch)
- Every push triggers automatic deployment
- Zero-downtime reload supported by Render

---

## 🛡 Production Readiness
- Gunicorn used instead of Flask development server
- Strict feature schema validation
- Graceful model loading & error handling
- Environment-agnostic deployment

---

## 👨‍💻 Author
**Muhammad Yousaf Khan**
Machine Learning Engineer
GitHub: https://github.com/yusiKhan

## Deployment

For full deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

This project demonstrates a complete end-to-end ML system:
EDA → Model → Serialization → Cloud Deployment