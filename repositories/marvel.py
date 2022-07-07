from typing import Union, Dict

import requests

from fastapi import status

import logger
from constans import MARVEL_BASE_URL
from models.marvel_respository import Comic


def find_comic_by_id(comic_id: int) -> Union[Comic, None]:
    try:
        url = f"{MARVEL_BASE_URL}/searchComics"
        params = {"comic_id": comic_id}
        response = requests.get(url=url, params=params)
        if response.status_code == status.HTTP_200_OK:
            response_json = response.json()
            if response_json["comics"]:
                comic = response_json["comics"][0]
                return Comic(
                    id=comic["id"],
                    title=comic["title"],
                    image=comic["image"],
                    onsaleDate=comic["onsaleDate"],
                )
    except Exception as e:
        logger.err("repositories/users.py", "find_user_by_token", f"error: {str(e)}")
