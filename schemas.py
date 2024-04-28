from pydantic import BaseModel
from typing import Optional, List

class KelvBase(BaseModel) : 
    class Config: 
        orm_mode = True

# includes fields exclusiveto orginals
class PaintingCreate (KelvBase) : 
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    price: float
    info: str
    galleryLink: Optional[str] = None
    galleryName: Optional[str] = None
    pages: Optional[List[str]] = None

# for returning a basic painting object
class Painting (KelvBase) : 
    id: int
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    price: float
    info: str

class Original (KelvBase) : 
    id: int
    title: str
    type: str
    dimensions: str
    # sold: bool # this will be false so no point returning it.. right? 
    giclee: bool
    price: float
    info: str
    galleryLink: Optional[str] = None
    galleryName: Optional[str] = None

class PageItem (KelvBase):
    id: int
    page: str
    painting_id: int
    page_order: int



