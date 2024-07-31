from flask import Flask, request
import joblib
import numpy as np
from sklearn.datasets import load_iris

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

# Load the Iris dataset target names
iris = load_iris()  # Load the Iris dataset
target_names = iris.target_names  # Extract the target names

@app.route("/", methods=["GET"])
def read_root():
    return {"message": "Welcome to the ML Model API"}

@app.route("/predict/", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = target_names[prediction][0]
    return {"class": class_name}

if __name__ == "__main__":
    app.run(debug=True)