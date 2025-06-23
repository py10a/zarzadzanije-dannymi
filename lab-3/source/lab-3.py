from flask import Flask, render_template
from flask_restful import Api, Resource
from student import StudentNames, AllNames
from security import authenticate, identity
from flask_jwt import JWT

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWT(app, authenticate, identity)

# student.py
api.add_resource(StudentNames, "/students/<string:name>")
api.add_resource(AllNames, "/students")

if __name__ == '__main__':
    app.run(debug=True)