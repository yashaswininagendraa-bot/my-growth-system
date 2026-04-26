import pytest
from server import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Backend is running"}

def test_assert_true():
    assert True