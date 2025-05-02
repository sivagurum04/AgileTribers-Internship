def validate_password(password):
    if len(password) < 8 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        raise ValueError("Password must be at least 8 characters long and contain both letters and numbers.")
validate_password("kj23")