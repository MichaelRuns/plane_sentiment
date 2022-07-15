from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import math
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


class LogisticRegression:
    theta = {}
    lr = 0.01
    num_epochs = 3
    n = 3

    def __init__(self):
        self.theta = {}
        self.lr = 0.03
        self.num_epochs = 10
        self.n = 3

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def extract_data(self, path):
        fp = open(path)
        line = fp.readline()
        line = fp.readline()
        ret = []
        while line != "":
            ex = line.split(sep=',')
            if len(ex) < 3:
                line = fp.readline()
                continue
            dic_form = {}
            label = 0
            if ex[1] == "positive":
                label = 1
            tweet = ex[2]
            for index in range(2,len(ex)):
                tweet = tweet + ex[index]
            tweet = tweet[:-1]
            index = 0
            while index + self.n < len(tweet):
                wrd = tweet.replace(" ", "")[index:index + self.n]
                if wrd in dic_form:
                    dic_form[wrd] = dic_form[wrd] + 1
                else:
                    dic_form[wrd] = 0
                index += 1
            ret.append((dic_form, label))
            line = fp.readline()
        fp.close()
        return ret


    def fit(self, path):
        print('training!')
        dataset = self.extract_data(path)
        for epoch in range(self.num_epochs):
            for example in dataset:
                for wrd in example[0].keys():
                    if wrd in self.theta:
                        self.theta[wrd] = self.theta[wrd] + (self.lr * (example[1] - self.sigmoid(example[0][wrd])) * (self.sigmoid(example[0][wrd]) * (1 - self.sigmoid(example[0][wrd]) * example[0][wrd])))
                    else:
                        self.theta[wrd] = 0
        self.theta[""] = 0
        print('finished')

    def predict(self, rev):
        prediction = "[please train classifier]"
        total = 0
        index = 0
        count = 0
        while index + self.n < len(rev):
            ngram = rev.replace(" ", "")[index:index + self.n]
            count += 1
            if ngram in self.theta:
                total += self.theta[ngram]
                # print(ngram + ": " + str(self.theta[ngram]))
            index += 1
        total /= count
        print(total)
        print(self.sigmoid(total))
        if self.sigmoid(total) > 0.5:
            prediction = "positive"
        else:
            prediction = "negative"

        return f"I predict that '{rev}' has {prediction} sentiment.", str(self.sigmoid(total))



lr = LogisticRegression()
templates = Jinja2Templates(directory="api/templates")
lr.fit('airline_sentiment_analysis.csv')


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return "please go to ./form for the interactive code!"


@app.post("/form")
def predict(request: Request, test: str = Form(...)):
    prediction, sigma = lr.predict(test)
    return templates.TemplateResponse('index.html', context={'request': request, 'prediction': prediction, 'sigma': sigma})


@app.get("/form")
def predict(request: Request):
    prediction = "Type a review"
    return templates.TemplateResponse('index.html', context={'request': request, 'prediction': prediction})







