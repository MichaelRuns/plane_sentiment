from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

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


@app.get("/")
def home():
    return "hello"


@app.get("/{review}")
def predict(review: str):
    return lr.predict(review)





