from flask import render_template, Blueprint

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/')
def index():
    return render_template("index.html")

@routes.route('/contact')
def contact():
    return render_template("contact.html")

@routes.route('/projects')
def projects():
    return render_template("projects.html")

@routes.route('/exp')
def experience():
    return render_template("experience.html")

"""
@routes.route('/skills')
def skills():
    return render_template("skills.html")
"""