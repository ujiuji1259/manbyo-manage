from dataclasses import asdict, dataclass

from pydantic import BaseModel
from typing import Optional, List
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from search import DiseaseSeacher
from util import load_dic
from manage_database import add_search_query

# build searcher
manbyo = load_dic("resource/dic.csv")
searcher = DiseaseSeacher(manbyo)


class SearchText(BaseModel):
    name: str

app = FastAPI()


origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/search")
async def search(data: SearchText):
    search_text = data.name
    if search_text is None:
        search_text = ""

    add_search_query(search_text)

    results = searcher.search(search_text)
    return [asdict(r) for r in results][:20]

@app.post("/submit_mistake")
async def submit_mistake(data: SearchText):
    name = data.name
    if True:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"text": "ok"})
