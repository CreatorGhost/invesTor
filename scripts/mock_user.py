from get_price_list import get_coin_data
import pymongo
import json
from time import sleep
import random
import string
from random_username.generate import generate_username

# Setting up the connection to the database


# Connection to database
cluster = pymongo.MongoClient()
db = cluster["crypto"]
collection = db["userData"]


def get_avatar():
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=5))
    avatar_url = f"https://api.multiavatar.com/{res}.png"
    return avatar_url




def get_icon(symbol):
    icon_url = f"https://assets.coincap.io/assets/icons/{symbol}@2x.png"
    return icon_url


coins = [{"name": "bitcoin", "apy": 5.46, "amount": 0.12093, "icon": get_icon("btc")},
         {"name": "solana", "apy": 15.46, "amount": 25, "icon": get_icon("sol")},
         {"name": "ethereum", "apy": 9.46, "amount": 1.18093, "icon": get_icon("eth")},
         {"name": "tether", "apy": 12.59, "amount": 456, "icon": get_icon("usdt")},
         {"name": "binance-coin", "apy": 5.46, "amount": 282.78, "icon": get_icon("bnb")},
         {"name": "xrp", "apy": 15.46, "amount": 0.12093, "icon": get_icon("xrp")},
         {"name": "polkadot", "apy": 8.87, "amount": 0.12093, "icon": get_icon("dot")}]

data = {"user_id": generate_username()[-1],
        "user_name": generate_username()[-1],
        "user_avatar": get_avatar(),
        "total_investment": 4100000,
        "total_return": 1204,
        "available_coins": coins
        }

collection.insert_one(data)
