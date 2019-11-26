import jsonify
from flask import Flask, request
from flask_restful import Resource, Api

from .modules.db import con_db

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class dbControl(Resource):
    def get(self, search):
        return con_db.GetData('QID', search)
    def put(self, faq):
        return PutData(request.get_json())

