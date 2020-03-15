from flask import Flask, Blueprint
from routes import routes

app = Flask(__name__)

app.register_blueprint(routes)

def connect():

    with open('C://Users//Yan//Desktop//Scripting//doenteMental.py//kaggle scrapper//mongo_str.txt', 'r') as f:
        mongo_str = f.read()
        
    client = MongoClient(mongo_str)
    db = client.kaggle
    return db


if __name__ == '__main__':
    app.secret_key='hiddenpass'
    app.run(debug=True)