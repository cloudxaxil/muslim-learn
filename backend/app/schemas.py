from pydantic import BaseModel
from typing import Literal



class User_register(BaseModel):
    email: str
    password: str
    name: str
    role: Literal["student", "teacher"]

class UserLogin(BaseModel):
    email: str
    password: str


class BookmarkRequest(BaseModel):
    surah_number: int
    ayah_number: int