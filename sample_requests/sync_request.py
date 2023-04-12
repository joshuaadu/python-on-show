import httpx
import requests
from fastapi.responses import Response


def get_user_request(base_url: str, endpoint_prefix: str, user_id: int) -> Response:
    url = base_url + endpoint_prefix + str(user_id)
    response = requests.get(url)
    return response


# get_response = httpx.get("http://localhost:8000/users/?start=0&limit=2", headers={})
# print("Get User response status code:", get_response.status_code)
# print("Get User response body:", get_response.json())
#
# post_data = {
#     "title": "string",
#     "description": "string",
#     "address": "string",
#     "roles": [
#         {
#             "name": "string",
#             "id": 0,
#             "description": "string"
#         }
#     ],
#     "name": "string",
#     "age": 23,
#     "department": "string"
# }
# post_response = httpx.post("http://localhost:8000/users/", headers={}, json=post_data)
# print("Add User response status code:", post_response.status_code)
# print("Add User response headers:", post_response.status_code)
# print("Add User response body:", post_response.json())
