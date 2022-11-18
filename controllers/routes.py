from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from run import app
import time


@app.route("/")
def index():
    time.sleep(4)
    return render_template("index.html")


@app.route("/login")
def login():
    
    return render_template("login.html")



@app.errorhandler(404) 
def not_found(e): 
  
  return render_template("404.html") 

@app.errorhandler(500) 
def internal_error(e): 
  
  return render_template("500.html")