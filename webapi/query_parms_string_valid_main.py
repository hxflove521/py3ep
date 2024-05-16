from typing import Annotated

from fastapi import FastAPI, Query

# swagger UI生成q参数时不是list
# https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.SkipJsonSchema

from pydantic.json_schema import SkipJsonSchema

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | SkipJsonSchema[None], 
                                  Query(
                                      title="查询参数",
                                      description="这是查询参数的一个描述",
                                      min_length=3,
                                      alias="item_query"
                                      )] = None):
    query_items = {"q": q}
    return query_items