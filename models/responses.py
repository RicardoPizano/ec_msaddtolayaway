from pydantic import BaseModel

from models.marvel_respository import Comic


class AddComicToLayawayResponse(BaseModel):
    user_id: str
    user_name: str
    comic: Comic


class ErrorResponse(BaseModel):
    message: str
