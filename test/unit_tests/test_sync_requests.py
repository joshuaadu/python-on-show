import responses
from sample_requests.sync_request import get_user_request


@responses.activate
def test_get_and_parse_user_works_properly():
    base_url = "http://localhost:8000"
    endpoint_prefix = "/users/"
    user_id = 0

    responses.add(
        responses.GET,
        f"{base_url}{endpoint_prefix}{user_id}",
        json={"user_id": user_id},
        status=200,
        # headers={}
    )

    response = get_user_request(base_url, endpoint_prefix, user_id)
    print(response.json())
    # assert response.status_code == 200
    assert response.status_code == 200

