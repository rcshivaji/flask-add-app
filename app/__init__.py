from flask import Flask, render_template, request

app = Flask(__name__)

def add_numbers(a, b):
    return a + b


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        result = add_numbers(num1, num2)
        return render_template(
            "result.html",
            num1=num1,
            num2=num2,
            result=result
        )
    return render_template("index.html")
