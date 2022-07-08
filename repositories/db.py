from pymongo.collection import Collection

import logger
from models.marvel_respository import Comic


def add_comic_to_layaway(db_session: Collection, user_uuid: str, comic: Comic) -> None:
    try:
        user_exist = db_session.layaways.find({user_uuid: {"$exists": True}})
        user = list(user_exist)
        if user:
            comic_exist = db_session.layaways.find({"_id": user[0].get("_id"), f"{user_uuid}.id": comic.id})
            if not list(comic_exist):
                db_session.layaways.update_one(
                    {"_id": user[0].get("_id")},
                    {"$push": {user_uuid: comic.dict()}}
                )
        else:
            db_session.layaways.insert_one({
                user_uuid: [comic.dict()]
            })
    except Exception as e:
        logger.err("repositories/db.py", "add_comic_to_layaway", f"error on save layaway: {str(e)}")
        raise e
