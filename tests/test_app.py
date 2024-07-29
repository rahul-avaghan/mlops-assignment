import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict(client):
    response = client.post('/predict', json=[[0, 0], [1, 1]])
    assert response.status_code == 200
    assert response.json == {'prediction': [0, 1]}
