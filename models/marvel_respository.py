from pydantic import BaseModel


class Comic(BaseModel):
    id: int
    title: str
    image: str
    onsaleDate: str
