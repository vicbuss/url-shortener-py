from flask import render_template, request

def shorten() -> str:
    if request.method == "POST":
        slug = 'abcde'
        short_url = f"http://127.0.0.1:5000/{slug}"
        return render_template("shortened.html", short_url = short_url)

    return render_template("index.html")