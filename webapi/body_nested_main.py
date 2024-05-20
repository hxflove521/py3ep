from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, AnyUrl

app = FastAPI()


class Image(BaseModel):
    url : AnyUrl
    name : str

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    tags : set[str] = set()
    image : Image | None = None

class Offer(BaseModel):
    name : str
    description : str | None = None
    price : float
    items : list[Item]   

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id":item_id, "item":item}
    return result

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/images/multiple/")
async def create_multiple_images(images:list[Image]):
    for image in images:
        image.url
    return images