from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model (NOT a DataFrame)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert input JSON to DataFrame
    input_data = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(input_data)

    return jsonify({
        "prediction": prediction[0]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

