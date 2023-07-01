from fastapi import FastAPI, APIRouter
from mangum import Mangum

from api.Dev import router as Dev_router   

app = FastAPI()
api_router = APIRouter(prefix="/dev")

@app.get('/healthcheck')
async def health_check():
    return {'message': 'OK'}

api_router.include_router(Dev_router)
app.include_router(Dev_router)

handler = Mangum(app)