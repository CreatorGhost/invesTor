from fastapi import FastAPI, Response, HTTPException, status, APIRouter, Depends
import pymongo
from bson import Binary, Code

router = APIRouter(tags=["Users"])

cluster = pymongo.MongoClient("mongodb+srv://aditya:cwwGe6sIS1rzQzTB@cluster0.aumcmvr.mongodb.net/?retryWrites=true&w=majority")
db = cluster["crypto"]
user_collection = db["userData"]


def get_data():
    result = []
    user_data = user_collection.find()
    for data in user_data:
        data["_id"] = str(data['_id'])
        result.append(data)
    return result


def update_data(user_id, amount,coin_name):
    user_collection.update_one({"user_id": user_id}, {"$inc": {f"available_coins.0.{coin_name}": amount}})
    print("data updated")

update_data("pacifiedBaboon0",5.4,"bitcoin")


@router.get('/userDetail')
def user_detail():
    return get_data()[-1]


# @router.put('/deposit')
# def user_detail():
#     return get_data()
