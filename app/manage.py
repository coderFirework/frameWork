from app import create_app
from app import  db
from model.NavModel import User

app=create_app()

if __name__=='__main__':
    app.run("127.0.0.1",5000)

