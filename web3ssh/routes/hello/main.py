from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def hello():
    return "Hello, world!"


@router.get("/world")
async def world():
    return "Hello, nigga!"
