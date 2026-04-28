import pytest
import requests

@pytest.fixture
def posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response

@pytest.fixture
def post1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response

@pytest.fixture
def users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response