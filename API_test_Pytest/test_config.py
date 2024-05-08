# test_config.py

import pytest
import requests

@pytest.fixture
def base_url():
    return "https://testwebsite.com/api/users"

@pytest.fixture
def valid_user_data():
    return {
        "id": 1101,
        "name": "Sowjanya Kanike",
        "email": "sowjanya.kanike@test.com"
    }

@pytest.fixture
def invalid_user_id():    return '12345'  # Invalid user ID that does not exist in the system
