from flask import Flask, Blueprint
from routes import routes

app = Flask(__name__)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.secret_key='hiddenpass'
    app.run(debug=True)