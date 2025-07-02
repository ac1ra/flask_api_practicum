from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime
import locale


@app.route("/")
def form():
    locale.setlocale(locale.LC_ALL, 'ru_RU')

    current_time = datetime.now()
    return render_template("home.html", current_time_html=current_time)


@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members_html=team_members)


dict_storage = {}


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        message_check = "Your message has been sen successfully!"
        name = request.form.get("name")
        email = request.form.get("email")
        city = request.form.get("city")
        street = request.form.get("street")
        post_zip = request.form.get("post_zip")
        message = request.form.get("message")

        dict_storage['name'] = name
        dict_storage['email'] = email
        dict_storage['city'] = city
        dict_storage['street'] = street
        dict_storage['post_zip'] = post_zip
        dict_storage['message'] = message

        return render_template("page.html", message_check_html=message_check, dict_storage_html=dict_storage)
    else:
        return redirect(url_for("/contact"))
