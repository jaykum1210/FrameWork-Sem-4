from flask import Flask

app = Flask(__name__)

@app.route("/")
def fun():
    return "Hello Code"

@app.route("/user/<name>")
def user_name(name):
    return f"Hello {name}"

@app.route("/user/<name>/<float:amt>")
def user_amount(name, amt):
    return f"Hello {name}, your amount is: {amt}"


@app.route("/course/")
@app.route("/course/string:<name>")
def course_detail(name = "Flask"):
    return f"Course Name : {name}"