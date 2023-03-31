
def test_user_me(testing_app):
    response = testing_app.get(f"/users/me")
    assert response.status_code == 200

