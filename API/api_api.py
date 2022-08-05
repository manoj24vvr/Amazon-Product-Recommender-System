from fastapi import FastAPI
import recommend
app = FastAPI()

@app.get('/recommend')
def recommender(input):
    a = recommend.result(input)
    return a