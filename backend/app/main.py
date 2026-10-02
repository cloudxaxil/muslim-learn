from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import client
from app.router.auth import router as auth_router
from app.router.quran_api import router as quran_router
from fastapi.middleware.cors import CORSMiddleware
from app.router.bookmarks import router as bookmarks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: run before requests

    await client.admin.command('ping')
    print("Application starting...")

    yield  # App is ready to handle requests

    # Shutdown: run after requests
    client.close()
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(bookmarks_router, prefix="/api/bookmarks")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(quran_router, prefix="/api/quran")

@app.get("/health")

def status_check():
    return {"status": "Healthy"}
