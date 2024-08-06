import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

# Set our tracking server URI for logging
# Run this MLflow server in the terminal before starting the code
# mlflow server --host 127.0.0.1 --port 8080
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
mlflow.set_experiment("Iris Classifier - Experiments")
mlflow.sklearn.autolog()

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define hyperparameters
n_estimators = 100
max_depth = None
min_samples_split = 5
min_samples_leaf = 2
max_features = 'auto'

# Train a random forest classifier with specified hyperparameters
model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    min_samples_split=min_samples_split,
    min_samples_leaf=min_samples_leaf,
    max_features=max_features
)

# Start an MLflow run
with mlflow.start_run():
    # Log hyperparameters
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("min_samples_split", min_samples_split)
    mlflow.log_param("min_samples_leaf", min_samples_leaf)
    mlflow.log_param("max_features", max_features)

    # Fit the model
    model.fit(X, y)

    # Log the model
    mlflow.sklearn.log_model(model, "random_forest_model")

    # Save the trained model to a file
    joblib.dump(model, 'model.joblib')
