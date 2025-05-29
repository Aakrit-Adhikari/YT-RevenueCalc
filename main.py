from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            views = int(request.form["views"])
            rpm = float(request.form["rpm"])
            earnings = (views / 1000) * rpm
            result = f"Estimated Earnings: ${round(earnings, 2)}"
        except:
            result = "Invalid input. Please enter numbers only."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)



