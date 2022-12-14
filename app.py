from flask import Flask, render_template, send_file, request, session, redirect

app = Flask(__name__)

register = {}

program_name = "My Website"

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
  
  return render_template("/index.html", title=program_name)

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    name_req = request.form.get("login")
    pass_req = request.form.get("pass")
    
    print(name_req, pass_req)
    
    if is_logged(name_req, pass_req):
      session["login"] = name_req
      session["pass"] = pass_req
      
      return redirect("/")
    
    return render_template("/login.html", title=program_name + " | Login", apologize="<p class='apologize'>Account not registered.</p>")
  
  return render_template("/login.html", title=program_name + " | Login")

@app.route("/register", methods=["GET", "POST"])
def register():
  return render_template("/register.html", title=program_name + " | Register")

# ---

def is_logged(login, passw):
  return False

def login(login, passw):
  pass