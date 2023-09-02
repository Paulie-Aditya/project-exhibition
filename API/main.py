from fastapi import FastAPI

app = FastAPI()


#get method to send a get request to our API
# @app.get("/")
# async def root():
#     return {"message": "Hello World! Welcome to my API"}

'''
when we update we need to reload the server ie ctrl+c and then run 'uvicorn main:app' 
short-cut --> 'uvicorn main:app --reload'           
'''

# new path operation - represents retrieving social media posts

# @app.get("/input_get")
# def get_posts():
#     return {"message":"will return post_input"}

# @app.get("/output_get")
# def get_posts():
#     return {"message":"will return post_output"}

# @app.post("/input")
# def create_post():
#     return {"message":"user input (movie name)"}
# @app.post("/output")
# def create_post():
#     return {"message":"review"}

# @app.put("/update")
# def update_post():
#     return{}

@app.get("/")
def index():
    return {'data':'blog list'}

#list of all unpublished blogs
@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublised blogs"}

@app.get("/blog/{blog_id}")
def show(blog_id:int):  #(only integer value is allowed)--> error if not a int 
    #fetch blog with id = blog_id
    return {'data':blog_id}



@app.get("/blog/{blog_id}/comments")
def comments(blog_id):
    #fetch comments of blog with id = blog_id
    return {'data':{'1','2'}}