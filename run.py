import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index ():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/flaskcomponents.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", flask_components=data)

@app.route("/about/<component_name>")
def about_component(component_name):
    component = {}
    with open("data/flaskcomponents.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == component_name:
                component = obj
    return render_template("component.html", component=component)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True #NEVER TRUE in the final product, this is a security risk
    )