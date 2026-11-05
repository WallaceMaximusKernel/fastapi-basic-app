from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Mr. EndPoint!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}
