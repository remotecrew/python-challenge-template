from fastapi import APIRouter
from app.models.item import Item

router = APIRouter(prefix="/items", tags=["items"])

fake_db = []

@router.get("/")
def get_items():
    return fake_db

@router.post("/")
def create_item(item: Item):
    fake_db.append(item)
    return item
