def user_schema(user):
    return {
        "name": user[0],
        "last_name": user[1],
        "email": user[2],
        "description": user[3],
        "course": user[4],
        "year": user[5]
    }