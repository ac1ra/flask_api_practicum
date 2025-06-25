from flask import render_template, request, redirect, url_for
from app import app


@app.route("/")
def form():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        message_check = "Your message has been sen successfully!"
        name = request.form.get("name")
        email = request.form.get("email")
        text = request.form.get("text")

        return render_template("contact.html", name=name, email=email, text=text, message_check=message_check)
    else:
        return redirect(url_for("/contact"))
