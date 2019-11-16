from flask import Flask

app = Flask(__name__, instance_relative_config = True)

#setting up configuration
# app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
