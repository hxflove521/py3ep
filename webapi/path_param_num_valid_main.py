from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="这是路径的title",gt=0,le=10)],
    q: Annotated[ str | None, Query(alias="item_query")] = None,
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results
