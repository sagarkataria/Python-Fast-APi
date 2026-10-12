from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime

class Review(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    play_name:str = Field(index=True)
    reviewer_name:str
    rating:int = Field(ge=1,le=5)
    comment:str
    created_at:datetime=Field(default_factory=datetime.now)

class ReviewCreat(SQLModel):
    play_name:str
    review_name:str
    rating:int = Field(ge=1,le=5)
    comment:str

class Read(SQLModel):
    id:int
    play_game:str
    reviewer_name:str
    rating:int
    comment:str
    created_at:datetime

class ReviewUpdate(SQLModel):
    rating:Optional[int] = Field(default=None, ge=1, le=5)
    comment:Optional[str] = None
