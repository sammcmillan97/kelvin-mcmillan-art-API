
from sqlalchemy import  Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



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

    # Painting --> PageItem, 1:N
    page_items = relationship("PageItem", back_populates="painting")
    
    # Painting --> Giclee, 1:1
    child_giclee = relationship("Giclee", back_populates="giclee_parent_painting", uselist=False)



class PageItem(Base):
    __tablename__ = 'page_items'
    id = Column(Integer, primary_key=True)
    page = Column(String(256))
    painting_id = Column(Integer, ForeignKey('paintings.id'))
    page_order = Column(Integer)

   # PageItem <-- Painting, N:1
    painting = relationship("Painting", back_populates="page_items")



class Giclee(Base):
    __tablename__ = 'giclees'
    id = Column(Integer, primary_key=True)
    page_order = Column(Integer)
    painting_id = Column(Integer, ForeignKey('paintings.id'))

    # Giclee <-- Painting, 1:1 
    giclee_parent_painting = relationship ("Painting", back_populates="child_giclee", uselist=False)

    # Giclee --> GicleeOption, 1:N
    children_options = relationship("GicleeOption", back_populates="parent_giclee")



class GicleeOption(Base):
    __tablename__ = 'giclee_option'
    id = Column(Integer, primary_key=True)
    gicleeId = Column(Integer, ForeignKey('giclees.id'))
    option_attribute_id = Column(Integer, ForeignKey("giclee_option_attributes.id"))
    
    # GicleeOption <-- Giclee, N:1 
    parent_giclee = relationship("Giclee", back_populates="children_options")

    # GicleeOption <-- GicleeOptionAttributes, N:1 
    parent_attributes = relationship("GicleeOptionAttributes", back_populates="children_options")

   

class GicleeOptionAttributes(Base):
    __tablename__='giclee_option_attributes'
    id = Column(Integer, primary_key=True)
    dimensions=Column(String)
    price = Column(Integer)

    # GicleeOptionAttributes --> GicleeOption, 1:N
    children_options = relationship("GicleeOption", back_populates="parent_attributes")

