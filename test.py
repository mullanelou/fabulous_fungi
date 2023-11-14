# main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/test")
async def test():
 return {"greeting":"Hello world"}