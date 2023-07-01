from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter, Path

router = APIRouter(prefix="/info")


class Dev(BaseModel):
    name: str
    position: str
    age: int
    career: str
    blog: str
    github: str


pool = []

@router.get("")
async def info():
    return {"message": "안녕 여기는 개발자 풀 이름을 URL의 붙여서 조회해줘!, 추가는 docs를 붙여서 add탭에서", 
            "list": [dev["name"] for dev in pool]}

@router.get("{name}")
async def search_pool(name:str):
    for dev in pool:
        if dev["name"].lower() == name.lower():
            return dev
    return {"message": "조회 불가 add로 이동해서 추가해주세요!"}

@router.post("add")
async def add_dev(dev: Dev):
    pool.append(dev.dict())
    return "추가 성공!"
