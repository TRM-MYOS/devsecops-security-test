from fastapi import FastAPI
from src.routes.songs import router as songs_router


app = FastAPI(
    title="Mini Music Library",
    version="1.0.0",
    description="Demo application for DevSecOps security testing",
)


app.include_router(songs_router)


@app.get("/")
def root():
    return {
        "message": "Mini Music Library API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }