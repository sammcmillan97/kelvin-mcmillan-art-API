from pydantic import BaseModel
from typing import List

# why...? do we really need inheritance here. 
class Painting():
    title: str
    class Config:
        orm_mode = True


class GetPaintings(BaseModel):
    title:  str
    class Config:
        orm_mode = True


class GetGiclees(BaseModel):
    title: str
    class Config:
        orm_mode = True


class GetPortFolioPage(BaseModel):
    paintings: List[Painting]

    class Config:
        orm_mode = True
