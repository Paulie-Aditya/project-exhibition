from fastapi import FastAPI

app = FastAPI()


#get method to send a get request to our API
@app.get("/")
async def root():
    return {"message": "Hello World! Welcome to my API"}

'''
when we update we need to reload the server ie ctrl+c and then run 'uvicorn main:app' 
short-cut --> 'uvicorn main:app --reload'           
'''

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