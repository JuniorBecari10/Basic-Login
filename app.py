from flask import Flask, render_template, send_file, request, session, redirect
from flask_session import Session

registers = []
program_name = "My Website"

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# <p class="apologize">Account not registered.</p>

# ---

@app.route("/style.css")
def style():
  return send_file("static/style.css")

# ---

@app.route("/")
def index():
  if not session.get("login") or session.get("pass"):
    return redirect("/login")
  
  return render_template("/index.html", title=program_name)

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    name_req = request.form.get("login")
    pass_req = request.form.get("pass")
    
    if is_logged(name_req, pass_req):
      session["login"] = name_req
      session["pass"] = pass_req
      
      return redirect("/")
    
    return render_template("/login.html", title=program_name + " | Login")
  
  return render_template("/login.html", title=program_name + " | Login")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    name_req = request.form.get("login")
    pass_req = request.form.get("pass")
    
    login(name_req, pass_req)

    session["login"] = name_req
    session["pass"] = pass_req
    
    return redirect("/")
  
  return render_template("/register.html", title=program_name + " | Register")

@app.route("/logout")
def logout():
  session["login"] = None
  session["pass"] = None
  
  return redirect("/login")

# ---

def is_logged(login, passw):
  global registers
  
  for reg in registers:
    if reg[0] == login and reg[1] == passw:
      return True
  
  return False

def login(login, passw):
  global registers
  
  registers.append((login, passw))