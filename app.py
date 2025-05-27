from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('heart_disease_model.pkl')
except FileNotFoundError:
    print("Error: heart_disease_model.pkl not found. Make sure the model file is in the correct directory.")
    model = None # Handle case where model is not found
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded."}), 500

    data = request.get_json()

    # Convert input data to a pandas DataFrame (adjust column names and order as needed)
    # **IMPORTANT:** The order of columns in the DataFrame MUST match the order
    # of features your model was trained on. If you're unsure, you'll need
    # to check how your model was trained and potentially reorder the columns
    # here or ensure the input data is sent in the correct order from the frontend.
    try:
        input_data = pd.DataFrame([data])
        # Example of explicitly ordering columns (uncomment and adjust if needed)
        # expected_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'] # Replace with your actual feature names in order
        # input_data = input_data[expected_columns]

    except Exception as e:
        return jsonify({"error": f"Error processing input data: {e}"}), 400


    # Make prediction
    try:
        # Assuming your model's predict_proba method returns probability of the positive class (1)
        prediction_probability = model.predict_proba(input_data)[:, 1][0]

    except Exception as e:
         return jsonify({"error": f"Error during prediction: {e}"}), 500


    # --- Add General Tips and Suggestions Here ---
    # These are general tips and should not be considered medical advice.
    general_tips = [
        "Maintain a healthy diet rich in fruits, vegetables, and whole grains.",
        "Engage in regular physical activity (e.g., brisk walking, jogging, swimming).",
        "Manage stress through techniques like meditation, deep breathing, or yoga.",
        "Ensure you get enough quality sleep.",
        "Avoid smoking and exposure to second-hand smoke.",
        "Limit your intake of saturated and trans fats, sugar, and salt.",
        "Monitor your blood pressure and cholesterol levels as recommended by your doctor.",
        "If you have diabetes, manage your blood sugar levels.",
        "Maintain a healthy weight.",
        "Consult with a healthcare professional for personalized advice and regular check-ups."
    ]
    # -------------------------------------------

    return jsonify({
        "prediction": float(prediction_probability), # Ensure it's a standard float
        "tips": general_tips # Include tips in the response
    })


if __name__ == '__main__':
    # Ensure you run this script within your Nix shell to have Flask and other dependencies available.
    # The host='0.0.0.0' makes the server accessible externally (useful in some environments,
    # but for local development 127.0.0.1 is usually sufficient and more secure).
    # Use debug=True for development to see error messages in the browser,
    # but set debug=False in a production environment.
    app.run(debug=True)
