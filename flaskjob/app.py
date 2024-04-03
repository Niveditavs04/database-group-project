from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/login")
def login():
    return render_template("index1.html")

@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/experience")
def dashboard():
    return render_template("dashboard.html")
if __name__ == "__main__":
    app.run(debug=True)