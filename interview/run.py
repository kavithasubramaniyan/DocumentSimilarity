'''
Author:Kavitha Subramaniyan
Module:run.py
Description:Module to invoke the similarity score app
'''
import uvicorn

if __name__=='__main__':
    uvicorn.run('main:app',host='localhost',port=8080,reload=True)