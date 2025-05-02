import logging

logging.basicConfig(
    filename='error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_password(password):
    try:
        if len(password) < 8 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            raise ValueError(f"Password '{password}' must be at least 8 characters long and contain both letters and numbers.")
        print("Password is valid.")
    except ValueError as e:
        logging.error(e)
        print("Validation failed. Error logged.")
validate_password("kj23")
validate_password("abcde123")