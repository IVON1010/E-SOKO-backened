<<<<<<< HEAD
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"])


@app.get('/')
def read_root():
    return {"Hello" : "world"}


@app.get('/orders')
def orders():
    
    orders = Orders.find_all()
    
    return orders



@app.get("/get_image")
async def get_image():
    image_path = Path("image.jpg")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)


@app.post('/users')
def users(data: UsersModel):
    
    users = Users(data.name, data.email, data.password, data.address) 
    

    


=======
from flask import Flask
from flask_migrate import Migrate
from models import db, User


app = Flask(__name__)

migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)
>>>>>>> d0d49fb5e2e78ce8b0db4d34414d8be9e961a14d
