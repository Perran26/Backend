# API HERE
from os import name
from flask import Flask, jsonify, request 

app= Flask(__name__)

@app.get('/user')
def get_all_user():
    user_data = users_db
    if user_data:
        return jsonify(user_data), 200
    else:
        return { "response": "That resource could not be found!"}, 404

@app.post('/getuser')
def create_new_user():
    input= request["name"]
    email=input["email"]
    user_id=create_user(users_db, name, email)

    user=get_user(user_id)


    if user:
        return jsonify(get_user(user_id)), 200
    else:
        return{ "Response": "Failed to create a new user!" }, 404   
    
    @app.get('/user/<int: user_id>')
    def get_user_by_id(user_id):
        user_data = get_user(user_id)

        if user_data:
            return jsonify(user_data), 200
        else:
            return { " response ": "A user with that ID was not found!" }, 400
        
    @app.delete('/user/<int:user_id>')
    def delete_user(user_id):
        if delete_user(user_id):
            return { "Responce": " A user with id: {user_id} was deleted!"}, 200
        else:
            return {" response": f"Failed to delete user with id:{user_id}"}, 400
# get    /users
# post   /user
# get    /user/123
# delete /user/123

# Fake Database
users_db = [
    {
        "user_id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
]

def get_user(user_id):
    for user in users_db:
        if user["user_id"] == user_id:
            return user
    return False

def create_user(users, name, email):
    new_id = len(users) + 1
    new_user = { "user_id": new_id, "name": name, "email": email }
    users_db.append(new_user)
    return new_id

def update_user(user_id, name="", email=""):
    for user in users_db:
        if user["user_id"] == user_id:
            if name != "":
                user["name"] = name
            if email != "":
                user["email"] = email

def delete_user(user_id):
    for user in users_db:
        if user["user_id"] == user_id:
            users_db.remove(user)
            return True
    return False
