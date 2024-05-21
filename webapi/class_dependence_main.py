# Before diving deeper into the Dependency Injection system, let's upgrade the previous example.

from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q:str |None = None,skip:int = 0, limit:int=100):
    return {"q":q, "skip":skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: Annotated[dict,Depends(common_parameters)]):
    return commons

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q:str |None=None, skip:int=0, limit:int=100) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit
        

@app.get("/items_new/")
async def read_items(commons: Annotated[CommonQueryParams,Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q":commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items":items})
    return response