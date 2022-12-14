from flask import Flask, render_template, send_file, request, session, redirect

app = Flask(__name__)

register = {}

# <p class="apologize">Account not registered.</p>

# ---

@app.route("/style.css")
def style():
  return send_file("static/style.css")

# ---

@app.route("/")
def index():
  if not session.get("login"):
    return redirect("/login")
  
  return render_template("/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    pass
  
  return render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
  return render_template("/register.html")

# ---