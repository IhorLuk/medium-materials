from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def first_response():
    return {"response": "first"}