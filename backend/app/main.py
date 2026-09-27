from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import client
from app.router.auth import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: run before requests

    await client.admin.command('ping')
    print("Application starting...")

    yield  # App is ready to handle requests

    # Shutdown: run after requests
    await client.close()
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix="/api/auth")

@app.get("/health")

def status_check():
    return {"status": "Healthy"}

