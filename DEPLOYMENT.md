# 🚀 Vehicle Price Estimator – Deployment Guide

This document explains how the Vehicle Price Estimator ML application is deployed in production using **Render.com**.

---

## 🔧 Tech Stack

* **Python 3.12**
* **Flask** (Backend Framework)
* **Scikit-Learn** (ML Pipeline)
* **Pandas & NumPy** (Data Processing)
* **Gunicorn** (Production WSGI Server)
* **Render.com** (Cloud Hosting)

---

## 📦 Project Structure

.
├── app.py
├── model.pkl
├── requirements.txt
├── render.yaml
├── templates/
├── static/
└── DEPLOYMENT.md


---

## 🤖 Model Details

* **Training:** Scikit-Learn pipeline.
* **Preprocessing:** Handled internally (categorical encoding + scaling).
* **Serialization:** Serialized using \`joblib\`.
* **Safety:** Loaded safely at runtime with validation & fallback checks.

**Model Version:** v1.0

---

## ☁️ Render Deployment

### Build Settings

**Build Command**

pip install -r requirements.txt


**Start Command**

gunicorn app:app


### ❤️ Health Check

The application exposes a health endpoint:


/healthz


* **Purpose:** Used by Render to verify service availability and manage routing.

### 🔄 Auto Deployment

* Connected to **GitHub** (main branch).
* Every push triggers automatic deployment.
* **Zero-downtime reload** supported by Render.

---

## 🛡 Production Readiness

* **Server:** Uses \`Gunicorn\` instead of the default Flask development server for concurrency.
* **Validation:** Strict feature schema validation.
* **Stability:** Graceful model loading & error handling.
* **Portability:** Environment-agnostic deployment configuration.

---

## 👨‍💻 Author

**Muhammad Yousaf Khan**
*Machine Learning Engineer*

**GitHub:** [https://github.com/yusiKhan](https://github.com/yusiKhan)

> **Project Summary:**
> This project demonstrates a complete end-to-end ML system:
> EDA → Model → Serialization → Cloud Deployment
