
from sqlalchemy import  Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# TABLES: 


class Painting(Base):
    __tablename__ = 'paintings'
    id = Column(Integer, primary_key=True)
    title = Column(String(256), unique=True)
    location = Column(String(256))
    type = Column(String, nullable=False)
    dimensions = Column(String, nullable=False)
    sold = Column(Boolean, nullable=False)
    framed = Column(Boolean, default=False)
    giclee = Column(Boolean, default=False)
    price = Column(Float)
    info = Column(String)
    galleryName = Column(String, nullable=True)
    galleryLink = Column(String, nullable=True)

    # Relationship with PageItem
    # note bp singular
    page_items = relationship("PageItem", back_populates="painting")



class PageItem(Base):
    __tablename__ = 'page_items'
    id = Column(Integer, primary_key=True)
    page = Column(String(256))
    painting_id = Column(Integer, ForeignKey('paintings.id'))
    page_order = Column(Integer)

    # painting_id from Painting id
    # note bp plural
    painting = relationship("Painting", back_populates="page_items")

