from fastapi import APIRouter, HTTPException
from src.database import songs

router = APIRouter(
    prefix="/songs",
    tags=["Songs"],
)


@router.get("/")
def get_songs():
    return songs


@router.get("/{song_id}")
def get_song(song_id: int):
    for song in songs:
        if song["id"] == song_id:
            return song

    raise HTTPException(
        status_code=404,
        detail="Song not found",
    )