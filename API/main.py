from fastapi import FastAPI
from Routers import covid

app = FastAPI()
app.include_router(covid.router)

@app.get("/")
def raiz():
    return {
        "message":"Welcome to the CovidPI"
    }