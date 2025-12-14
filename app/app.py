
from flask import Flask, request, jsonify
from app.model import MLModel
import logging

app = Flask(__name__)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load ML model once at startup
model = MLModel()

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "features" not in data:
            return jsonify(
                {"error": "Invalid input. Expected JSON with 'features' key."}
            ), 400

        features = data["features"]

        if not isinstance(features, list) or len(features) != 2:
            return jsonify(
                {"error": "Features must be a list of two numeric values."}
            ), 400

        prediction = model.predict(features)

        logger.info("Prediction generated successfully")

        return jsonify(
            {
                "prediction": prediction
            }
        ), 200

    except Exception as e:
        logger.error("Error during prediction", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
