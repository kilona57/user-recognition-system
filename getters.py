def get_email() -> str:
    """
    Запрашивает у пользователя ввод email.
    
    Returns:
        str: Введенный пользователем email.
    """
    return input('Введите email: ')


def get_password() -> str:
    """
    Запрашивает у пользователя ввод пароля.
    
    Returns:
        str: Введенный пользователем пароль.
    """
    return input('Введите password: ')


def get_password_confirm() -> str:
    """
    Запрашивает у пользователя подтверждение пароля.
    
    Returns:
        str: Введенное пользователем подтверждение пароля.
    """
    return input('Подтвердите password: ')
