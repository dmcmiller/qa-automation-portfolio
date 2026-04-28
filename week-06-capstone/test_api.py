import pytest 
import re
import requests

## Status Code Validation

#Testing post endpoints
@pytest.mark.smoke
@pytest.mark.status
def test_post_endpoints(posts):
    assert posts.status_code == 200

#Testing user endpoints
@pytest.mark.smoke
@pytest.mark.status
def test_user_endpoints(users):
    assert users.status_code == 200

#test multiple post endpoints one after the other
@pytest.mark.status
@pytest.mark.parametrize('id', [2, 50, 100])
def test_post_response(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    assert response.status_code == 200


## Schema Validation

@pytest.mark.schema
@pytest.mark.smoke
def test_post_schema(posts):
    data = posts.json()
    required_keys = {'userId', 'id', 'title', 'body'}
    for post in data:
        assert required_keys.issubset(post.keys())

@pytest.mark.schema
@pytest.mark.smoke
def test_user_schema(users):
    data = users.json()
    required_keys = {'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'}
    for user in data:
        assert required_keys.issubset(user.keys()) 

@pytest.mark.schema
def test_single_post_is_dict(post1):
    post1_dict = post1.json()
    assert isinstance(post1_dict, dict)



## Data Validation

@pytest.mark.data
def test_post_data_types(posts):
    data = posts.json()
    for post in data:
        assert isinstance(post['userId'], int)
        assert isinstance(post['id'], int)
        assert isinstance(post['title'], str)
        assert isinstance(post['body'], str)

@pytest.mark.data
def test_email_validation(users):
    data = users.json()
    email_pattern = r"^\S+@\S+\.\S+$"
    for user in data:
        assert re.match(email_pattern, user['email'])

@pytest.mark.data
@pytest.mark.smoke
def test_post_collection_size(posts):
    data = posts.json()
    assert len(data) == 100

@pytest.mark.data
@pytest.mark.smoke
def test_users_collection_size(users):
    data = users.json()
    assert len(data) == 10

@pytest.mark.data
@pytest.mark.parametrize('id', [2, 50, 100])
def test_user_values_not_empty(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    data = response.json()
    for attribute in data:
        assert data[attribute] is not None and data[attribute] != ""


