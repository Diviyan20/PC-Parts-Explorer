def validate_string(text):
    special_characters = '"#$%^&*()-+?_=,!<>/'

    if any(c in special_characters for c in text):
        raise ValueError("Username/Full Name Cannot contain special characters")

    return True