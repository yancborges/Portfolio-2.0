from flask import render_template, Blueprint

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/')
def index():
    return render_template("index.html")

@routes.route('/contact')
def contact():
    return render_template("contact.html")
