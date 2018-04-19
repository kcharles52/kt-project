from flask import Flask
from .views.home import home #import home blue print


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py') #use variables in instance config
app.register_blueprint(home) #register the blue print
