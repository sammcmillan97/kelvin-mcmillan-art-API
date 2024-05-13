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


class GicleeOptionAttribute: 
    id: int
    dimensions: str
    price: int


class GicleeOption(KelvBase):
    option_attribute_id: int # should the UI recieve the id, or the full option attribute object...?
    gicleeId: int


class Giclee(KelvBase):
    id: int
    paintingId: int
    # can I just return a whole painting here?
    options: List[GicleeOption] # more complex object
    page_order: int

class GicleeCreate(KelvBase):
    paintingId: int
    page_order: int # does not have to be provided. Could use auto increment
    paintingId: int
    goa_ids: List[int] # when creating, provide a list of GOA ids



    



