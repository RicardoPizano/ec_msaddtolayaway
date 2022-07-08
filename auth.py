from typing import Tuple, Union

from models.users_repository import UserResponse
from repositories import users


def auth(authorization_header: str) -> Tuple[Union[UserResponse, None], bool]:
    if authorization_header:
        bearer_sections = authorization_header.split(" ")
        if len(bearer_sections) == 2 and bearer_sections[0].lower() == "bearer":
            token = bearer_sections[1]
            user = users.find_user_by_token(token=token)
            if user:
                return user, True
    return None, False
