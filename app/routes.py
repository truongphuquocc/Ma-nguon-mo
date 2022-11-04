# from crypt import methods
from turtle import title
from app import app
from flask import render_template, redirect,flash
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    # return "Hello World"
    user_info = {
        "city": "Hue"
    }
    title = {
        "title": "MyPage",
        "myRoute": "I❤️U"
    }
    number_list = {
        "one", "two", "three"
    }
    students_info = [
        {"name": "Thanh", "java": 8, "php": 7, "C": 9},
        {"name": "Bao", "java": 10, "php": 9, "C": 10},
        {"name": "Quoc", "java": 8, "php": 9, "C": 8}
    ]
    login_form = LoginForm()
    return render_template("index.html", user = user_info, title = title, students= students_info, form = login_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash(f"Uername: {login_form.username.data}")
        return redirect("index")
    return render_template("login.html", form = login_form)