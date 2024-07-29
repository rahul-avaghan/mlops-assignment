from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Dummy model (for demonstration purposes)
model = LogisticRegression()
model.fit(np.array([[0, 0], [1, 1]]), [0, 1])


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
