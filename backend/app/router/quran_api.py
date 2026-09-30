from fastapi import APIRouter
from app.core.database import db

router = APIRouter()

surahs_collection = db.surahs
ayahs_collection = db.ayahs

@router.get("/surahs")
async def get_all_surahs():
    surahs = await surahs_collection.find().to_list(length=None)
    for surah in surahs:
        surah.pop("_id")
    return surahs


@router.get("/surah/{surah_number}") # ayah
async def get_surah_ayahs(surah_number: int):
    ayahs = await ayahs_collection.find({"surah_number": surah_number}).to_list(length=None)
    for surah in ayahs:
            surah.pop("_id")
    return ayahs



@router.get("/audio/{reciter}/{surah_number}")

async def get_surah_recitation(surah_number : int, reciter: str):

    audio_url =   f"https://cdn.islamic.network/quran/audio-surah/128/{reciter}/{surah_number}.mp3"

    return {"audio_url": audio_url} 