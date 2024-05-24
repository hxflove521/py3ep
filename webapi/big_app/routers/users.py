from fastapi import APIRouter

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username":"张三"},{"username":"里斯"}]

@router.get("/user/me",tags=["users"])
async def read_user_me():
    return {"username":"fakecurrentuser"}

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username":username}
