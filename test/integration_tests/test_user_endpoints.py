def test_user_me(testing_app):
    response = testing_app.get(f"/users/me")
    assert response.status_code == 200


def test_get_valid_user(testing_app, valid_user_id):
    response = testing_app.get(f"/users/{valid_user_id}")
    assert response.status_code == 200


def test_delete_user_success(testing_app, valid_user_id):
    response = testing_app.delete(f"/users/{valid_user_id}")
    assert response.status_code == 200


def test_double_delete_user_fails(testing_app, valid_user_id):  # testing_app fixture function scope not working
    response_1 = testing_app.delete(f"/users/{valid_user_id}")
    assert response_1.status_code == 200  # bug: fails because a new testing_app was not initialized

    response_2 = testing_app.delete(f"/users/{valid_user_id}")
    assert response_2.status_code == 404


def test_delete_invalid_user_success(testing_app, invalid_user_id):
    response = testing_app.delete(f"/users/{invalid_user_id}")
    assert response.status_code == 404


def test_add_new_user_success(testing_app, new_user):
    response = testing_app.post(f"/users", json=new_user.dict())
    assert response.status_code == 201


def test_update_user_success(testing_app, updated_user, valid_user_id):
    response = testing_app.put(f"/users/{valid_user_id}", json=updated_user.dict())
    assert response.status_code == 200


def test_rate_limit_works(testing_app, testing_rate_limit, valid_user_id):
    for i in range(testing_rate_limit):
        response = testing_app.get(f"/users/{valid_user_id}")
        if "x-app-rate-limit" not in response.headers:
            assert response.status_code == 429




