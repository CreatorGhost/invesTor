import json
import requests
import pprint
from apy_intrest import var


def get_icon(symbol):
    icon_url = f"https://assets.coincap.io/assets/icons/{symbol}@2x.png"
    return icon_url


def parse_data(data):
    info = {
        "id": data["id"],
        "rank": int(data["rank"]),
        "symbol": data["symbol"],
        "name": data["name"],
        "priceUsd": round(float(data["priceUsd"]), 3),
        "priceChange": round(float(data["changePercent24Hr"]), 3),
        "icon": get_icon(data["symbol"].lower()),
        "apy": var[data['id']]["apy"],
        "interest": var[data['id']]["ints"]
    }

    return info


def parse_data_no_apy(data):
    info = {
        "id": data["id"],
        "rank": int(data["rank"]),
        "symbol": data["symbol"],
        "name": data["name"],
        "priceUsd": round(float(data["priceUsd"]), 3),
        "priceChange": round(float(data["changePercent24Hr"]), 3),
        "icon": get_icon(data["symbol"].lower()),
    }

    return info


def format_data(data_lst):
    coin_lst = []
    for data in data_lst:
        tmp = parse_data_no_apy(data)
        coin_lst.append(tmp)
    return coin_lst


def get_coin_data(limit=10):
    url = "http://api.coincap.io/v2/assets"
    params = {"limit": limit}
    response = requests.request("GET", url, params=params)
    res = json.loads(response.text)
    formatted_res = format_data(res["data"])
    return formatted_res

# print(call_api(3))
# pprint.pprint(call_api(15))
# resp = call_api(15)
# #
# for i in resp:
#     print(f"{i['id']} APY {var[i['id']['apy']]} ")
