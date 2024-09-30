from fastapi import FastAPI

app = FastAPI()



@app.get("/api-endpoint")
async def fisrt_api():
    return {"message": "Hello Eric!"}