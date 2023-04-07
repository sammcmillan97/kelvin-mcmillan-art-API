# main.py
from typing import List
from uuid import uuid4

from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="Sam",
         last_name="McMillan",
         gender=Gender.male,
         roles=[Role.admin]
         ),
    User(id=uuid4(),
         first_name="Angus",
         last_name="McMillan",
         gender=Gender.male,
         roles=[Role.admin]
         ),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
