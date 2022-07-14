from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates

app = FastAPI()


class LogisticRegression:
    theta = {}

    def __init__(self):
        self.theta = {}

    def fit(self, path):
        pass

    def predict(self, rev):
        return "prediction from: " + rev


lr = LogisticRegression()
templates = Jinja2Templates(directory="api/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{review}")
def predict(review: str):
    return lr.predict(review)





