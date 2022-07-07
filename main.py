from typing import Union

import pymongo
from fastapi import FastAPI, Response, status, Header

import logger
from constans import MONGO_URL
from models.requests import AddComicToLayawayRequest
from auth import auth
from models.responses import ErrorResponse, AddComicToLayawayResponse
from repositories import marvel, db
from schemas_responses import add_to_layaway_response

app = FastAPI()

LOGGER_FILE_NAME = "main.py"

client = pymongo.MongoClient(MONGO_URL)
db_session = client.ecdb_comics


@app.post("/addToLayaway", responses={**add_to_layaway_response})
async def add_comic_to_layaway(r: Response,
                               request: AddComicToLayawayRequest,
                               authorization: Union[str, None] = Header(dfault=None)):
    user, authenticated = auth(authorization_header=authorization)
    if not authenticated:
        r.status_code = status.HTTP_401_UNAUTHORIZED
        return ErrorResponse(message="bearer auth invalid")
    if not request.comic_id:
        r.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorResponse(message="comic_id is required")
    comic = marvel.find_comic_by_id(comic_id=request.comic_id)
    if not comic:
        r.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponse(message="comic not fund")
    try:
        db.add_comic_to_layaway(db_session=db_session, user_uuid=user.id, comic=comic)
    except Exception as e:
        logger.err(LOGGER_FILE_NAME, "add_comic_to_layaway", f"error on save layaway: {str(e)}")
        r.status_code = status.HTTP_409_CONFLICT
        return ErrorResponse(message="error on save layaway")
    return AddComicToLayawayResponse(
        user_id=user.id,
        user_name=user.name,
        comic=comic,
    )
