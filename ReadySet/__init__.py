# ReadySet/__init__/py

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy 
app = Flask(__name__, instance_path='/ReadySet/instance/')

app.config.from_object('ReadySet.config')
app.config.from_pyfile('config.py')

#app.register_blueprint(auth_api)

db = SQLAlchemy(app)

import ReadySet.auth_views

if __name__ == '__main__':
		app.run(port=5000,debug=True)
