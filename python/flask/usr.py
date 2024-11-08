def get_user_by_id(user_id, users):
    """if user dictionary is founf return otherwise Nine."""
    for user in users:
        if user.get('id') == user_id:
            return user
    return None

#exeample usage
users = [
    {"id": 1, "name": "Njoki"},
    {"id": 2, "name": "Mwaura"},
    {"id": 3, "name": "Kimami"}
]

user = get_user_by_id(1, users)
print(user)

user = get_user_by_id(3, users)
print(user)