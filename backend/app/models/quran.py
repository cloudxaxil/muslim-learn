from typing import Literal
from pydantic import BaseModel


class Surah(BaseModel):
    number: int
    name_arabic: str
    name_english : str
    ayah_count : int
    revelation_type : Literal["Meccan", "Medinan"]


class Ayah(BaseModel):
    surah_number : int
    ayah_number: int
    text_arabic : str
    translation_english : str