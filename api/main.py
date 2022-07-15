from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()


class LogisticRegression:
    theta = {}

    def __init__(self):
        self.theta = {}

    def fit(self, path):
        print('training!')
        pass

    def predict(self, rev):
        prediction = "[please train classifier]"
        rev = str(rev)
        print(rev)
        if rev[0] == 'y':
            prediction = "the first letter is y!"
        else:
            prediction = 'the first letter is not y!'
        return "The result is:  " + prediction


lr = LogisticRegression()
templates = Jinja2Templates(directory="api/templates")
lr.fit('asdf')


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return "please go to ./form for the interactive code!"


@app.post("/form")
def predict(request: Request, test: str = Form(...)):
    prediction = lr.predict(test)
    return templates.TemplateResponse('index.html', context={'request': request, 'prediction': prediction})


@app.get("/form")
def predict(request: Request):
    prediction = "Type a review"
    return templates.TemplateResponse('index.html', context={'request': request, 'prediction': prediction})







