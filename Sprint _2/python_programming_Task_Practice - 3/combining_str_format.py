def validate_password_verbose(password):
    if len(password) < 8:
        raise ValueError(f"Error: The password '{password}' is too short. It must be at least 8 characters long.")
    if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        raise ValueError(f"Error: The password '{password}' must contain both letters and numbers.")
print(validate_password_verbose("jhgfhkg76"))