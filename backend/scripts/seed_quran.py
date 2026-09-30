import requests
import asyncio
from app.core.database import db
import time

surahs_collection = db.surahs
ayahs_collection = db.ayahs


async def seed_surah():
    for surah_number in range(1, 115):
        response = requests.get(f'http://api.alquran.cloud/v1/surah/{surah_number}')

        data = response.json()
        surah_info = data["data"]
        Translation_response = requests.get(f'http://api.alquran.cloud/v1/surah/{surah_number}/en.asad')
        translation_data = Translation_response.json()
        translation_surah_info =  translation_data["data"]

        for arabic_ayah, translated_ayah in zip(surah_info["ayahs"], translation_surah_info["ayahs"]):
            ayah_document = {
            "surah_number": surah_info["number"],    
            "ayah_number": arabic_ayah["numberInSurah"],
            "text_arabic": arabic_ayah["text"],
            "translation_english": translated_ayah["text"]
            }
            await ayahs_collection.insert_one(ayah_document)
        surah_document = {
        "number": surah_info["number"],
        "name_arabic": surah_info["name"],
        "name_english": surah_info["englishName"],
        "ayah_count": surah_info["numberOfAyahs"],
        "revelation_type": surah_info["revelationType"]
        }
        await surahs_collection.insert_one(surah_document)
        print(f"Seeded surah {surah_number}")
        time.sleep(0.5)


if __name__ == "__main__":
    asyncio.run(seed_surah())
    print("Done seeding surah 1")