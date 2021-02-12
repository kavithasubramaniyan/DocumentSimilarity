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

@app.on_event("startup")
async def startup_event():
    logger.info('starting up.....')

@app.post("/document-similarity",tags=['Similarity_Score'])
async def document_similarity(doc1:str,doc2:str):

    return {"message": "Two documents are compared",
            "doc1":doc1,
            "doc2":doc2,
            "Similarity score":fetch.compute_similarity(doc1,doc2)

            }