from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = 10.5
    tags : list[str] = []
    

@app.post("/items/",response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get("/items/",response_model=list[Item])
async def read_item() -> Any:
    return [
        Item(name="Apple", price=44.3),
        Item(name="Pear", price= 55.5),
    ]
    

class UserOut(BaseModel):
    username : str
    email : EmailStr
    full_name : str | None = None

class UserIn(UserOut):
    password: str
    

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id:str):
    return items[item_id]

@app.get("/items/{item_id}/name",
         response_model=Item,
         response_model_include={"name", "description"})
async def read_item_name(item_id:str):
    return items[item_id]


@app.get("/items/{item_id}/public",
         response_model=Item,
         response_model_exclude={"tax"})
async def read_item_name(item_id:str):
    return items[item_id]