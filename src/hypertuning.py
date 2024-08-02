import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid with valid max_features options
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None]  # Valid options for max_features
}

# Create a RandomForestClassifier
rf = RandomForestClassifier(random_state=42)

# Set up the GridSearchCV
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=2)

# Fit GridSearchCV
grid_search.fit(X_train, y_train)

# Best parameters found by GridSearchCV
print("Best parameters found:", grid_search.best_params_)

# Best cross-validated score
print("Best accuracy score:", grid_search.best_score_)

# Best model
best_rf_model = grid_search.best_estimator_

# Predict on the validation set
y_pred = best_rf_model.predict(X_val)

# Evaluate the model
#Evaluate the model test 111
accuracy = accuracy_score(y_val, y_pred)
print(f"Validation set accuracy: {accuracy:.2f}")


# Save the best model
joblib.dump(grid_search.best_estimator_, 'best_model.joblib')
