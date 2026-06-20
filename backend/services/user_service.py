from models.users import insert_user, delete_user
from utils.validators import validate_string

def register_account(username, email, full_name, password):
    try:
        validate_string(username)
        validate_string(full_name)
        
        record = insert_user(username, email, full_name, password) 
        print(f"New user {username} has been created successfully!")
        return record
    
    except Exception as e:
        raise ValueError("Failed to create new user:", e)

def delete_account(username, password):
    try:
        validate_string(username)
        validate_string(password)

        record = delete_user(username, password)
        print(f"User {username} has been deleted.")
        return record

    except Exception as e:
        raise ValueError("Failed to delete user:", e)