'''
Author:Kavitha Subramaniyan
Module:main.py
Description:API to find the similarity between two documents using FastAPI framework
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
import logging
from logic import fetch
from pydantic import BaseModel


logger=logging.getLogger(__name__)
app = FastAPI(
     title="Document Similarity",
     description="App to identify how similar two documents are",
    version=1.0,
    docs_url="/")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ProxyHeadersMiddleware)

class Item(BaseModel):
    document1: str
    document2:str

@app.on_event("startup")
async def startup_event():
    logger.info('starting up.....')
    
 
@app.post("/document-similarity",tags=['Similarity_Score'])
async def document_similarity(item: Item):
               return {"Similarity score":fetch.compute_similarity(item.document1,item.document2)}