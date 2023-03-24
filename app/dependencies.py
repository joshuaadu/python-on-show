from fastapi import (
    Response,
    HTTPException,
)
import time


start_time = time.time()
reset_interval = 10
limit = 5
count = 0


def rate_limit(response: Response) -> Response:
    global count
    global start_time

    if time.time() > start_time + reset_interval:
        start_time = time.time()
        count = 0
    if count >= limit:
        raise HTTPException(status_code=429, detail={"error": "Rate limit exceeded",
                                                     "timeout": round(start_time + reset_interval - time.time())
                                                     })
    count += 1
    response.headers["X-limit"] = f"{count}:{limit}"
    return response
