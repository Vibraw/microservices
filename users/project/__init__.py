
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!',
            'status_' : 'false'
        }

api.add_resource(UsersPing, '/users/ping')

if __name__ == '__main__':
    app.run(debug=True)