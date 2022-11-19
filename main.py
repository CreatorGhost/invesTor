from random_username.generate import generate_username
from get_price_list import get_coin_data
from requests import Request, Session
from routers import user,coins

import json
# from web3 import Web3

from fastapi import FastAPI, Response, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel, EmailStr
from typing import Optional
from random import randint
import pymongo
from typing import List, Union

# Fill in your infura API key here
# infura_url = "https://mainnet.infura.io/v3/a379d81dcbae48bcb7a613bf9d335587"
# web3 = Web3(Web3.HTTPProvider(infura_url))


app = FastAPI()


app.include_router(user.router)
app.include_router(coins.router)

