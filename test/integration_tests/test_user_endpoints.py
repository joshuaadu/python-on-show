
# def test_user_me(testing_app):
#     response = testing_app.get(f"/users/me")
#     assert response.status_code == 200


def test_delete_user_success(testing_app, valid_user_id):
    response = testing_app.delete(f"/users/{valid_user_id}")
    assert response.status_code == 200


def test_double_delete_user_fails(testing_app, valid_user_id):  # testing_app fixture function scope not working
    response_1 = testing_app.delete(f"/users/{valid_user_id}")
    print(response_1.json())
    assert response_1.status_code == 200    # bug: fails because a new testing_app was not initialized

    response_2 = testing_app.delete(f"/users/{valid_user_id}")
    print(response_2.json())
    assert response_2.status_code == 404


def test_delete_invalid_user_success(testing_app, invalid_user_id):
    response = testing_app.delete(f"/users/{invalid_user_id}")
    assert response.status_code == 404

