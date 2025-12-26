import os
import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------------------------------------------------
# 1. CONFIGURATION & SCHEMA DEFINITION
# ---------------------------------------------------------
MODEL_PATH = 'model.pkl'

# STRICT ORDER: Must match X_train.columns.tolist() exactly
EXPECTED_COLUMNS = [
    'Brand', 'Model', 'Year', 'CarAge', 'Condition', 'Mileage(km)',
    'EngineSize(L)', 'FuelType', 'Horsepower', 'Torque', 'Transmission',
    'DriveType', 'BodyType', 'Doors', 'Seats', 'Color', 'Interior',
    'City', 'AccidentHistory', 'Insurance', 'RegistrationStatus',
    'FuelEfficiency(L/100km)'
]

# METADATA: Defines the UI structure and options based on your dataset
FORM_SCHEMA = {
    'Brand': {
        'label': 'Car Brand', 'type': 'select',
        'options': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Hyundai', 'Kia', 'Volkswagen', 'BMW', 'Mercedes-Benz',
                    'Audi', 'Tesla', 'Porsche', 'Mazda', 'Nissan', 'Fiat', 'Renault', 'Peugeot', 'Dacia']
    },
    'Model': {
        'label': 'Model Name', 'type': 'text', 'placeholder': 'e.g. Corolla, Civic, F-150'
    },
    'Year': {
        'label': 'Year of Manufacture', 'type': 'number', 'min': 1990, 'max': 2026
    },
    'CarAge': {
        'label': 'Vehicle Age (Years)', 'type': 'number',
        'readonly': True, 'placeholder': 'Auto-calculated from Year'
    },
    'Condition': {
        'label': 'Condition', 'type': 'select', 'options': ['New', 'Used', 'Damaged']
    },
    'Mileage(km)': {
        'label': 'Mileage (km)', 'type': 'number', 'min': 0
    },
    'EngineSize(L)': {
        'label': 'Engine Size (L)', 'type': 'number', 'step': '0.1'
    },
    'FuelType': {
        'label': 'Fuel Type', 'type': 'select', 'options': ['Gasoline', 'Diesel', 'Hybrid', 'Electric']
    },
    'Horsepower': {
        'label': 'Horsepower (HP)', 'type': 'number', 'min': 0
    },
    'Torque': {
        'label': 'Torque (Nm)', 'type': 'number', 'min': 0
    },
    'Transmission': {
        'label': 'Transmission', 'type': 'select', 'options': ['Automatic', 'Manual']
    },
    'DriveType': {
        'label': 'Drive Type', 'type': 'select', 'options': ['FWD', 'RWD', 'AWD']
    },
    'BodyType': {
        'label': 'Body Type', 'type': 'select',
        'options': ['Sedan', 'SUV', 'Hatchback', 'Pickup', 'Coupe', 'Convertible', 'Wagon']
    },
    'Doors': {
        'label': 'Doors', 'type': 'select', 'options': [2, 3, 4, 5]
    },
    'Seats': {
        'label': 'Seats', 'type': 'select', 'options': [2, 4, 5, 6, 7, 8]
    },
    'Color': {
        'label': 'Exterior Color', 'type': 'select',
        'options': ['White', 'Black', 'Gray', 'Silver', 'Blue', 'Red', 'Brown', 'Other']
    },
    'Interior': {
        'label': 'Interior Material', 'type': 'select', 'options': ['Leather', 'Cloth', 'Other']
    },
    'City': {
        'label': 'City', 'type': 'text', 'placeholder': 'e.g. New York, Tokyo'
    },
    'AccidentHistory': {
        'label': 'Accident History', 'type': 'select', 'options': ['No', 'Yes']
    },
    'Insurance': {
        'label': 'Insurance Status', 'type': 'select', 'options': ['Valid', 'Expired']
    },
    'RegistrationStatus': {
        'label': 'Registration', 'type': 'select', 'options': ['Complete', 'Incomplete']
    },
    'FuelEfficiency(L/100km)': {
        'label': 'Fuel Efficiency', 'type': 'number', 'step': '0.1'
    }
}

# ---------------------------------------------------------
# 2. MODEL LOADING
# ---------------------------------------------------------
model = None


def load_model():
    """Safely loads the model pipeline."""
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print(f"✅ Model loaded successfully from {MODEL_PATH}")
        else:
            print(f"⚠️  WARNING: {MODEL_PATH} not found in root directory.")
    except Exception as e:
        print(f"❌ Error loading model: {e}")


# ---------------------------------------------------------
# 3. ROUTES
# ---------------------------------------------------------

@app.route('/', methods=['GET'])
def index():
    """Renders the dynamic input form."""
    return render_template('index.html', columns=EXPECTED_COLUMNS, schema=FORM_SCHEMA)


@app.route('/predict', methods=['POST'])
def predict():
    """Handles data processing and prediction."""
    if not model:
        load_model()
        if not model:
            return render_template('result.html', error="Model file not found. Please upload model.pkl.")

    try:
        input_data = {}

        # Harvest data from form, strictly adhering to EXPECTED_COLUMNS order
        for col in EXPECTED_COLUMNS:
            val = request.form.get(col)
            config = FORM_SCHEMA.get(col, {})

            # Smart Type Conversion
            if config.get('type') == 'number' or col in ['Doors', 'Seats']:
                input_data[col] = float(val) if val else 0.0
            else:
                input_data[col] = val

        # Create DataFrame (This is what the pipeline expects)
        df = pd.DataFrame([input_data])

        # PREDICTION
        # The pipeline handles Scaling/Encoding internally
        prediction = model.predict(df)[0]

        # Formatting output
        formatted_price = f"${prediction:,.2f}"

        return render_template('result.html', prediction=formatted_price, details=input_data)

    except Exception as e:
        # Graceful error handling
        return render_template('result.html', error=f"Prediction Error: {str(e)}")


if __name__ == "__main__":
    app.run()
