from pydantic import BaseModel
from typing import List

# why...? do we really need inheritance here. 
class Painting(BaseModel):
    id: int
    title: str
    type: str
    dimensions: str
    sold: bool
    giclee: bool
    image_url: str
    price: str

    class Config:
        orm_mode = True


class GetPaintingsResponse(BaseModel):
    paintings: List[Painting]
    class Config:
        orm_mode = True


class GetOriginalsResponse(BaseModel):
    title: str
    class Config:
        orm_mode = True


class GetPortfolioPageResponse(BaseModel):
    paintings: List[Painting]
    class Config:
        orm_mode = True


class GicleeOption(BaseModel):
    dimensions: str
    price: str
    class Config:
        orm_mode = True



class Giclee(BaseModel):
    painting: Painting
    options: List[GicleeOption]
    class Config:
        orm_mode = True


class GetGicleesResponse(BaseModel):
    paintings: List[Giclee]
    class Config:
        orm_mode = True
