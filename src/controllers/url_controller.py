from flask import render_template

def index() -> str:
    return render_template("index.html")

def shorten() -> str:
    return render_template("shortened.html")