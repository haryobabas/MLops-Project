import pytest
import requests

from main import app, TextInput


@pytest.fixture(scope="module")
def api_url():
    return "http://localhost:8080"


def test_index(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200
    assert response.json() == {
        "status": {
            "code": 200,
            "message": "Success fetching the API"
        }
    }
def test_predict_ham(api_url):
    input_data = {"text": "This is a test email"}
    response = requests.post(f"{api_url}/predict", json=input_data)
    assert response.status_code == 200
    assert response.json() == {"prediction": "Ham"}

def test_predict_spam(api_url):
    input_data = {"text": "This is promotion email to get discount"}
    response = requests.post(f"{api_url}/predict", json=input_data)
    assert response.status_code == 200
    assert response.json() == {"prediction": "Spam"}





if __name__ == "__main__":
    pytest.main([__file__])