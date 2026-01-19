from flask import Flask


app = Flask(__name__)

@app.route("/home/<jay>")
def fun(jay):
    return "Hello" +jay+  "I am Flask Here"

if __name__== "__main__":
    app.run(debug=True)
