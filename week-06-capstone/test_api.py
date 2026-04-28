import pytest 


#Testing post endpoints
def test_post_endpoints(posts):
    assert posts.status_code == 200

#Testing user endpoints
def test_user_endpoints(users):
    assert users.status_code == 200

