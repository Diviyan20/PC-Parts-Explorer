from models.users import insert_user
from utils.validators import validate_string

def create_user(username, email, full_name, password):
    try:
        validate_string(username)
        validate_string(full_name)
        
        record = insert_user(username, email, full_name, password) 
        print(f"New user {username} has been created successfully!")
        return record
    
    except Exception as e:
        print("Failed to create new user:", e)