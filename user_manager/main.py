from flask import Flask
from flask_restful import Resource, Api
from main_db import create_db_connection
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
create_db_connection()
Base = declarative_base()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
