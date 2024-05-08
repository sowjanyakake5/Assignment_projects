# test_user_api.py

import pytest
import requests

def test_get_user_data(base_url, valid_user_data):
    user_id = valid_user_data["id"]
    response = requests.get(f"{base_url}/{user_id}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    user_data = response.json()
    assert user_data["id"] == user_id, f"Expected user ID {user_id}, but got {user_data['id']}"
    assert user_data["name"] == valid_user_data["name"], f"Expected name '{valid_user_data['name']}', but got '{user_data['name']}'"
    assert user_data["email"] == valid_user_data["email"], f"Expected email '{valid_user_data['email']}', but got '{user_data['email']}'"

def test_invalid_user_id(base_url, invalid_user_id):
    response = requests.get(f"{base_url}/{invalid_user_id}")
    assert response.status_code == 404, f"Expected status code 404 for invalid user ID, but got {response.status_code}"
