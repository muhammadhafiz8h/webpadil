from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

USERNAME = "admin"
PASSWORD = "12345"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        if user == USERNAME and pw == PASSWORD:
            session["login"] = True
            return redirect("/home")
    return render_template("login.html")

@app.route("/home")
def home():
    if not session.get("login"):
        return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
