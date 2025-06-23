from flask_restful import Resource
from user import User

users = [
    User("admin", "admin", 1),
    User("user", "user", 2),
]

username_table = {user.username: user for user in users}
user_id_table = {user.id: user for user in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password == password:
        return user
    return None

def identity(payload):
    user_id = payload['identity']
    return username_table.get(user_id, None)


