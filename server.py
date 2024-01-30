from flask import Flask, render_template, request, redirect, session
#this is to import the __init__.py file
from flask_app import app 
#controller name (Doesn't need the .py at the end)
from flask_app.controllers import controller_name_here



if __name__=="__main__":   
# Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    
# Run the app in debug mode. Host is for Mac users due to AirPods