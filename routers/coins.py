from fastapi import FastAPI, Response, HTTPException, status, APIRouter, Depends
import pymongo
from bson import Binary, Code

router = APIRouter(tags=["Coins"])

cluster = pymongo.MongoClient("mongodb+srv://aditya:cwwGe6sIS1rzQzTB@cluster0.aumcmvr.mongodb.net/?retryWrites=true&w=majority")
db = cluster["crypto"]
collections = db["coinlist"]


def get_data():
    result = []
    user_data = collections.find()
    for data in user_data:
        data["_id"] = str(data['_id'])
        result.append(data)
    return result


@router.get("/coins")
def coin_list():
    return get_data()
