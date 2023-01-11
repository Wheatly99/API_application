from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Software engineering project'}


def test_predict():
    response = client.post("/predict/",
                           json={"text": "Меня зовут Алекс и я [MASK] в Екатеринбурге."}
                           )
    json_data = response.json()
    print(json_data)
    assert response.status_code == 200
    assert json_data["1"]["token_str"] == "живу"
