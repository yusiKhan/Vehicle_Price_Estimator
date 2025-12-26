# AutoValuate AI - Production Machine Learning App

A production-grade Flask application for serving the `Car Price Valuation` Scikit-learn pipeline.

## 📋 Features
- **Dynamic Form Engine**: UI is auto-generated from the feature schema in `app.py`.
- **Pipeline Integration**: Accepts raw inputs and passes a DataFrame to the pipeline (no hardcoded OneHotEncoding).
- **Smart Logic**: Frontend automatically calculates `CarAge` based on the dataset's reference year (2025).

## 🛠️ Setup & Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt