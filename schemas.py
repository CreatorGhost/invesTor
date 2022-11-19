from pydantic import BaseModel, EmailStr

from typing import List, Union, Optional


class CoinList(BaseModel):
    id: str
    rank: int
    symbol: str
    name: str
    priceUsd: float
    priceChange: float
    icon: str
    apy: float
    interest: float


class UserData(BaseModel):
    user_id: str
    user_name : str
    user_avatar : str
    total_investment: int
    total_return: int
    available_coins: List[CoinList]


class AddMovie(BaseModel):
    popularity: int
    director: str
    genre: List[str] = []
    imdb_score: float
    name: str


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str
    # set is admin as Optional
    is_admin: Optional[bool] = False
