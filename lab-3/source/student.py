from flask_restful import Resource
from flask_jwt import jwt_required

student_list = [
    {"name": "John", "age": 20, "city": "New York"},
    {"name": "Jane", "age": 21, "city": "Los Angeles"},
    {"name": "Jim", "age": 22, "city": "Chicago"},
]

class StudentNames(Resource):
    def get(self, name):
        for student in student_list:
            if student["name"] == name:
                return student
        return {"data": "Not found"}, 404

    def post(self, name):
        student = {"name": name}
        student_list.append(student)
        return student, 201
    
    def delete(self, name):

        for idx, student in enumerate(student_list):
            if student["name"] == name:
                student_list.pop(idx)
                return {"data": "Removed"}, 200
        return {"data": "Not found"}, 404
    

class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {"data": student_list}