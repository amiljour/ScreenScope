from flask_app import app
from flask import Flask, request, redirect, render_template, session, flash
# from flask_app.models.**model** import **Class**
from flask_bcrypt import Bcrypt

# Create a varible called bcrypt to call upon it later
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')