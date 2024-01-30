from flask import Flask

app = Flask(__name__)
#For session:
app.secret_key = 'shhh' #Set a secret key for security
#so that you can call the db with just the DB varible
DB = 'name_of_database_here'