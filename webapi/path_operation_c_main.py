# Response Status Code

from fastapi import FastAPI, status
from pydantic import BaseModel

from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

class Tags(Enum):
    items = "items"
    users = "users"

@app.post("/items/",response_model=Item, status_code=status.HTTP_201_CREATED,tags=[Tags.items])
async def create_item(item: Item):
    return item

@app.get("/items/", tags=[Tags.items], summary="Read an item.")
async def read_items():
    """
    Read an item.
    
    - **name**: 每个item都有自己的name.
    - **price**: 每个item的价格.
    """
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", 
         tags=[Tags.users],
         summary="读取用户信息", 
         description="Read user info,This is a description.",
         response_description="读取用户信息后返回结果",
         deprecated=True
)
async def read_users():
    return [{"username": "johndoe"}]