from fastapi import FastAPI, Response, HTTPException, status, APIRouter, Depends
import random

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["UsersAuth"])


@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends()):
    user_id = user.username
    if user_id is None:
        raise HTTPException(status_code=403, detail="Please provide valid credentials")

    # user_password = get_user(user_id)["password"]
    #
    # if not verify(password, user_password):
    #     raise HTTPException(status_code=403, detail="Please provide valid credentials")

    token = random.getrandbits(128)
    return {"token": token, "token_type": "bearer"}