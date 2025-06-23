from flask_restful import Resource


class User(Resource):
    def __init__(self, username, password, id):
        self.username = username
        self.password = password
        self.id = id 

    def __str__(self):
        return f"User(username={self.username}, password={self.password}, id={self.id})"

    def get(self):
        return {"data": self.username, "password": self.password, "id": self.id}, 200
    
    def post(self):
        return {"data": self.username, "password": self.password, "id": self.id}, 201
    
    def delete(self):
        return {"data": self.username, "password": self.password, "id": self.id }, 200