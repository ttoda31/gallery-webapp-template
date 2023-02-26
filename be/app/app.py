from pathlib import Path

from database import THUMBNAIL_DIR, Category, Item, Tag, get_db
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    return "Hello! This is FastAPI!"


@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items[:60]


@app.get("/categories")
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories[:60]


@app.get("/tags")
def read_tags(db: Session = Depends(get_db)):
    tags = db.query(Tag).all()
    return tags[:60]


@app.get("/item/thumbnail/{uid}")
def get_thumbnail(uid: str, db: Session = Depends(get_db)):
    row = db.query(Item.thumbnail_path).filter(Item.uid == uid).first()
    if row is None:
        return
    thumbnail_path = Path(THUMBNAIL_DIR) / Path(row.thumbnail_path)
    if thumbnail_path.exists():
        return FileResponse(thumbnail_path)
