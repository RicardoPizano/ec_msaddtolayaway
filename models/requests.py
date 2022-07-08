from typing import Union

from pydantic import BaseModel


class AddComicToLayawayRequest(BaseModel):
    comic_id: Union[int, None] = None
