from typing import List
from typing import Dict

def check_data(email: str, password: str, users: List[Dict[str, str]]) -> str:
    """
    Проверяет, существуют ли пользователь с указанными email и password.

    Args:
        email (str): Email пользователя.
        password (str): Password пользователя.
        users (List[Dict[str, str]]): Список существующих пользователей.

    Returns:
        str: Сообщение о результатах проверки.
    """
    for user in users:
        if user["email"] == email:
            if user["password"] == password:
                return email
            else:
                return "Ошибка: Неверные данные."
    return "Ошибка: Неверные данные."


def is_email_unique(email: str, users: List[Dict[str, str]]) -> bool:
    """
    Проверяет, является ли email уникальным среди существующих пользователей.

    Args:
        email (str): Email, который необходимо проверить.
        users (List[Dict[str, str]]): Список существующих пользователей.

    Returns:
        bool: True, если email уникальный, False - если email уже существует.
    """
    for user in users:
        if user["email"] == email:
            return False
    return True


def are_passwords_match(password: str, password_confirm: str) -> bool:
    """
    Проверяет, совпадают ли введенный пароль и его подтверждение.

    Args:
        password (str): Введенный пользователем пароль.
        password_confirm (str): Введенное пользователем подтверждение пароля.

    Returns:
        bool: True, если пароли совпадают, False - если пароли не совпадают.
    """
    return password == password_confirm
