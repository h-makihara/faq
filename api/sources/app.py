from flask import Flask, request
from flask_restful import Resource, Api
from apis.db import TodoSimple, dbControl
app = Flask(__name__)
api = Api(app)

api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(dbControl, '/db/<string:search>')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
