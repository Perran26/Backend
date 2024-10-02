# API HERE

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
