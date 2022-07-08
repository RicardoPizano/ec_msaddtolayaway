from typing import Union

import requests
from fastapi import status

import logger
from constans import USERS_BASE_URL
from models.users_repository import UserResponse


def find_user_by_token(token: str) -> Union[UserResponse, None]:
    try:
        url = f"{USERS_BASE_URL}/users"
        params = {"token": token}
        response = requests.get(url=url, params=params)
        if response.status_code == status.HTTP_200_OK:
            response_json = response.json()
            return UserResponse(
                id=response_json["id"],
                name=response_json["name"],
                age=response_json["age"],
                token=response_json["token"],
                password=response_json["password"],
            )
    except Exception as e:
        logger.err("repositories/users.py", "find_user_by_token", f"error: {str(e)}")
