from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name : str
    decription : str | None = None
    price : float
    tax : float | None = None

class User(BaseModel):
    username : str
    full_name : str | None = None
    
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="商品ID", ge=0,le=1000)],
    user : User,
    importance : Annotated[int, Body()],
    q : str | None = None,
    item : Item | None = None,
    ):
    results = {"item_id":item_id,"user": user, "importance": importance}
    if q :
        results.update({"q":q})
    if item:
        results.update({"item":item})
    return results
