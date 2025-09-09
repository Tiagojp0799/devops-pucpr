from fastapi import FastAPI

import random

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/random_number")
async def funcaoteste():
    return {"return": True, "random_number": random.randint(0,1000)}