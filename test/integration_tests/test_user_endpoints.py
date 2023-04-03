
# def test_user_me(testing_app):
#     response = testing_app.get(f"/users/me")
#     assert response.status_code == 200


def test_delete_user_success(testing_app, valid_user_id):
    response = testing_app.delete(f"/users/{valid_user_id}")
    assert response.status_code == 200


# def test_double_delete_user_fails(testing_app, valid_user_id):
#     response_1 = testing_app.delete(f"/users/{valid_user_id}")
#     assert response_1.status_code == 200
#
#     response_2 = testing_app.delete(f"/users/{valid_user_id}")
#     assert response_2.status_code == 404
#     assert response_2.json() == f"Non-existent user_id: {valid_user_id} was requested"

