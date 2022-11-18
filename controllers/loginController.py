from flask import render_template, redirect, request, flash, session
from config import app



@app.route("/logon", methods=["POST"])
def logon():

      # if form is submited
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password") 
        remember = request.form.get("remember") 

        print(username, password, remember )
        

        # Session On or Off - 7 Days
        # match remember:
        #     case "None":
        #         session.permanent = False
        #     case "on":
        #         session.permanent = True


        return redirect('/')



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")