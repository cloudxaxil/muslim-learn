from app.schemas import User_register
from fastapi import APIRouter
from app.core.security import hash_password
from app.core.database import db
from app.schemas import UserLogin
from fastapi import HTTPException
from app.core.security import  verify_password
from app.core.security import create_access_token

router = APIRouter()

users_collection = db.users

@router.post("/register")


async def Register_user(Payload: User_register):
    user = await users_collection.find_one({"email": Payload.email})
    if user :
        raise HTTPException(status_code=409, detail="Try different email, This email already registered")
    Data_storage =Payload.dict()
    hashed_password = hash_password(Payload.password)

    Data_storage["password"] = hashed_password

    await users_collection.insert_one(Data_storage)
    return "success"

@router.post("/login")

async def User_login(Payload: UserLogin):
    user = await users_collection.find_one({"email": Payload.email})
    if not user :
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(Payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": create_access_token(user["email"], user["role"]), "token_type": "bearer"}



