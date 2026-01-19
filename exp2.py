from flask import Flask

app = Flask(__name__)

@app.route("/")
def fun():
    return "Enter Number"

@app.route("/user/<int:amt>")
def amount(amt):
    total = 0
    for i in range(2,amt+1):
        found = 0
        for j in range(2,i):
            if i%j==0:
                found = 1
                break

        if found == 0:
            total+=i
    return f"Sum Of Prime Number Between 2 and {amt} = {total}"            