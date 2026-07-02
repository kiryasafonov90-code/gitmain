import requests
import pytest

BASE_URL = "https://postman-echo.com"

def test_get_with_params():
    # Проверка передачи параметров в GET-запросе
    params = {"user": "ivan", "id": 10}
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["args"] == params

def test_post_json_body():
    # Проверка отправки JSON-тела в POST-запросе
    body = {"message": "Hello World"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/post", json=body, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == body

def test_put_raw_text():
    # Проверка отправки обычного текста в PUT-запросе
    text_data = "This is a plain text"
    headers = {"Content-Type": "text/plain"}
    response = requests.put(f"{BASE_URL}/put", data=text_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["data"] == text_data

def test_delete_method():
    # Проверка корректного ответа на DELETE-запрос
    response = requests.delete(f"{BASE_URL}/delete")
    assert response.status_code == 200
    data = response.json()
    assert data["method"] == "DELETE"

def test_custom_headers():
    # Проверка получения сервером пользовательских заголовков
    custom_header = {"X-Custom-Header": "SecretValue"}
    response = requests.get(f"{BASE_URL}/get", headers=custom_header)
    assert response.status_code == 200
    data = response.json()
    assert data["headers"]["x-custom-header"] == "SecretValue"