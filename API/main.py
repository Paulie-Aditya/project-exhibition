from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#get method to send a get request to our API
# @app.get("/")
# async def root():
#     return {"message": "Hello World! Welcome to my API"}

'''
when we update we need to reload the server ie ctrl+c and then run 'uvicorn main:app' 
short-cut --> 'uvicorn main:app --reload'           
'''
#this is a test
# new path operation - represents retrieving social media posts

@app.get("/input_get")
def get_posts():
    return {"message":"will return post_input"}

@app.get("/output_get")
def get_posts():
    return {"message":"will return post_output"}

@app.post("/input")
def create_post():
    return {"message":"user input (movie name)"}
@app.post("/output")
def create_post():
    return {"message":"review"}

@app.put("/update")
def update_post():
    return{}



@app.get("/")
def index(limit=10, published:bool = True, sort: Optional[str]= None):
    return published
    if published:
        return {'data':f'{limit} published blog from the db'}
    else:
        return {'data':f'{limit} blog from the db'}

#list of all unpublished blogs
@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublised blogs"}

@app.get("/blog/{blog_id}")
def show(blog_id:int):  #(only integer value is allowed)--> error if not a int 
    #fetch blog with id = blog_id
    return {'data':blog_id}



@app.get("/blog/{blog_id}/comments")
def comments(blog_id, limit = 10):
    #fetch comments of blog with id = blog_id
    return limit
    return {'data':{'1','2'}}




#request body

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f'blog is created with title as {request.title}'}