from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your pre-trained model and columns
model = None
model_columns = None

def load_model():
    global model
    try:
        model = joblib.load("model.joblib")
    except (FileNotFoundError, Exception) as e:
        raise Exception(f"Error loading model: {e}")


# Load the model on startup
load_model()

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Train the model first."})

    try:
        # Get features from the request
        data = request.get_json()
        query = pd.get_dummies(pd.DataFrame([data]))
        query = query.reindex(columns=model_columns, fill_value=0)

        # Make prediction
        prediction = list(model.predict(query))[0]

        # Return prediction as JSON
        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
