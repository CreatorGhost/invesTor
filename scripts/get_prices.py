from get_price_list import get_coin_data
import pymongo
import json
from time import sleep
from random import randint

# Setting up the connection to the database


# Connection to database
cluster = pymongo.MongoClient()
db = cluster["crypto"]
collection = db["coinlist"]


def update_coin(coin_id, coin_detail):
    """
    This function updates a movie by name
    :param coin_id:
    :param coin_detail:
    :return:
    """
    collection.update_one({"id": coin_id}, {"$set": coin_detail})


def insert_data(data):
    for coins in data:
        update_coin(coins["id"], coins)



def add_data():
    coins_lst = get_coin_data(15)
    # for coins in coins_lst:
    collection.insert_many(coins_lst)


def keep_updating_data():

    while True:
        data = get_coin_data(15)
        insert_data(data)
        sleep(30)




insert_data(data)
