import httpx

get_response = httpx.get("http://localhost:8000/users/?start=0&limit=2", headers={})
print("Get User response status code:", get_response.status_code)
print("Get User response body:", get_response.json())

post_data = {
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
    "age": 23,
    "department": "string"
}
post_response = httpx.post("http://localhost:8000/users/", headers={}, json=post_data)
print("Add User response status code:", post_response.status_code)
print("Add User response headers:", post_response.status_code)
print("Add User response body:", post_response.json())
