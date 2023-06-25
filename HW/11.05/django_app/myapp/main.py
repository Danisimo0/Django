from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello():
    return "Hello from FastAPI!"
