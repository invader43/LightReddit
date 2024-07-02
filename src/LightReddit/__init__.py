from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configs
app.config['SECRET_KEY']= 'database-testing'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'




db = SQLAlchemy(app)




from LightReddit.main.routes import main

app.register_blueprint(main)