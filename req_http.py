import asyncio

import requests

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


def http_get_sync(url: str) -> JSONObject: #-> NON ASYNCHRONOUS
    response = requests.get(url) #-> response of the whole request
    return response.json()


async def http_get(url: str) -> JSONObject: #-> ASYNCHRONOUS
    return await asyncio.to_thread(http_get_sync, url) #-> executes it on a separate thread
#-> allows realize the request without blocking the loop of asyncio events. 
