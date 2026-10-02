from fastapi import Depends , APIRouter
from app.schemas import BookmarkRequest
from app.core.database import db
from app.core.dependencies import get_current_user

router = APIRouter()
bookmarks_collection = db.bookmarks

@router.post("/bookmark")
async def bookmark_ayah(Payload: BookmarkRequest, current_user: dict = Depends(get_current_user)):
    bookmark_document = {
    "email": current_user["email"],
    "surah_number": Payload.surah_number,
    "ayah_number": Payload.ayah_number
}
    await bookmarks_collection.insert_one(bookmark_document)
    return {"message": "Bookmark saved"}

@router.get("/bookmarks")
async def get_my_bookmarks(current_user: dict = Depends(get_current_user)):
    bookmarks = await bookmarks_collection.find({"email": current_user["email"]}).to_list(length=None)
    for bookmark in bookmarks:
                bookmark.pop("_id")
    return bookmarks

@router.delete("/bookmark")
async def remove_bookmark(Payload: BookmarkRequest, current_user: dict = Depends(get_current_user)):
    await bookmarks_collection.delete_one({
    "email": current_user["email"],
    "surah_number": Payload.surah_number,
    "ayah_number": Payload.ayah_number
})
    return {"message": "Bookmark removed"}