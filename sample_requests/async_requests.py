from httpx import AsyncClient
import asyncio
import aiohttp
from fastapi.responses import Response


async def sample_async_get_request(base_url: str, endpoint_prefix: str, user_id: int) -> (int, dict):
    url = f"{base_url}{endpoint_prefix}{user_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.json()
            print(response)
            # print(response.headers)
            status_code = response.status
            return status_code, json_response


# async def sample_async_get_request(base_url: str, endpoint_prefix: str, user_id: int) -> Response:
#     async with AsyncClient() as client:
#         response = await client.get('http://localhost:8000/users/me')
#         print(response)
#         print(response.headers)
#         print(response.json())
#         return response


async def sample_async_post_request():
    r_body = {
        "title": "string",
        "description": "string",
        "address": "string",
        "roles": [
            {
                "name": "string",
                "id": 0,
                "description": "string"
            }
        ],
        "name": "string",
        "age": 19,
        "department": "string"
    }
    async with AsyncClient() as client:
        response = await client.post('http://localhost:8000/users/', json=r_body)
        print(response)
        print(response.headers)
        print(response.json())

#
# asyncio.run(sample_async_get_request())
# asyncio.run(sample_async_post_request())
