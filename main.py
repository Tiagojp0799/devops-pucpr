from fastapi import FastAPI

import random

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/random_number")
async def random_number():
    """Generate and return a random integer between 0 and 1000."""
    return {"return": True, "random_number": random.randint(0,1000)}
