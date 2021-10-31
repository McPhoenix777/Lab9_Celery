from fastapi import FastAPI
from tasks import add
api = FastAPI()
@api.get("/addition")
async def addition():
    add.delay(10, 10)
    return {"message": "addition completed."}
