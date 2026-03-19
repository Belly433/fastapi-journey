from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class BorrowRecord(BaseModel):
    user_name: str = Field(..., min_length=2, max_length=50)
    borrow_date: date
    return_date: Optional[date] = None

class Book(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=2, max_length=50)
    year: int = Field(..., ge=1500, le=2100)
    borrow_records: List[BorrowRecord] = []