import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
# Set our tracking server uri for logging

# Run this mlflow server in the terminal before starting the code
# mlflow server --host 127.0.0.1 --port 8080
# mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
mlflow.set_experiment("Iris classifier")
mlflow.sklearn.autolog()

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a random forest classifier
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'model.joblib')
