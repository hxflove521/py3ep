from typing import Union

from fastapi import FastAPI, Cookie, Depends, Response
from typing_extensions import Annotated

app = FastAPI()


def query_extractor(q: Union[str, None]= None):
    return q

def query_or_cookie_extractor(
    q:Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()]=None,
):
    if not q:
        return last_query
    return q

@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
    response: Response
):
    #增加设置cookie，可快速测试效果
    response.set_cookie(key="last_query",value=query_or_default)
    return {"q_or_cookie":query_or_default}


