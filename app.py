from flask import Flask, request,redirect, url_for, Response, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/' , methods = ["GET", "POST"])

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials.try again", mimetype='text/plain')
    
    return '''
    <h2>Login Page</h2>
    <form method="post">
        Username: <input type="text" placeholder = "username" name="username"><br>
        Password: <input type="password" placeholder = "password"  name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''
##after login welcome page
@app.route('/welcome')
def welcome():
    if "user" in session:
        return f'''<h2>"Welcome {session['user']}!</h2><br>
        <a href = {url_for("logout")}>Logout</a>'''
    return redirect(url_for("login"))


#logout function
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

                    
              
           




    