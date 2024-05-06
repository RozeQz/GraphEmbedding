import re


def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        raise ValueError("Некорректный адрес электронной почты")
    return email


def validate_password(password):
    password = str(password)
    if len(password) < 8:
        raise ValueError("Пароль должен содержать хотя бы 8 символов")
    if not any(c.isalpha() for c in password):
        raise ValueError("Пароль должен содержать хотя бы 1 латинскую букву")
    if not any(c.isdigit() for c in password):
        raise ValueError("Пароль должен содержать хотя бы 1 цифру")
    return password
