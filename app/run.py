from flask import Flask, Blueprint, render_template
from routes import routes

app = Flask(__name__)

app.register_blueprint(routes)


"""
def connect():

    with open('C://Users//Yan//Desktop//Scripting//doenteMental.py//kaggle scrapper//mongo_str.txt', 'r') as f:
        mongo_str = f.read()
        
    client = MongoClient(mongo_str)
    db = client.kaggle
    return db
"""

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key='hiddenpass'
    app.run(debug=True)