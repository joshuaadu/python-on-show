import pytest
# import responses
from aioresponses import aioresponses
from sample_requests.async_requests import sample_async_get_request


@pytest.mark.asyncio
async def test_async_get_request():
    base_url = "http://localhost:8000"
    endpoint_prefix = "/users/"
    user_id = 0

    with aioresponses() as m:
        m.get(
            f"{base_url}{endpoint_prefix}{user_id}",
            payload={"user_id": user_id},
            status=200,
            # headers={}
        )

        status_code, json_response = await sample_async_get_request(base_url, endpoint_prefix, user_id)

    assert status_code == 200
    assert type(json_response["user_id"]) == int


