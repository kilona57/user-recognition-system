import json
from getters import get_email
from getters import get_password
from getters import get_password_confirm
from validators import check_data
from validators import is_email_unique
from validators import are_passwords_match

def get_user_choice() -> str:
    """
    Выводит меню выбора действий и запрашивает выбор пользователя.
    
    Returns:
        str: Выбранное пользователем действие.
    """
    print("""
    Выберите действие:
    1. Вход
    2. Регистрация 
    3. Выход (введите "exit" для выхода)
    """)
    return input("Введите номер действия или 'exit' для выхода: ")


def app():
    """
    Основной цикл приложения, реализующий функциональность регистрации и входа.
    """
    with open('users.json', 'r', encoding='UTF-8') as read_users_for_file:
        users = json.load(read_users_for_file)

    while True:
        choice = get_user_choice()

        if choice.lower() == "exit":
            print('Программа завершена.')
            break

        match choice:
            case "1":
                email = get_email()
                password = get_password()
                result = check_data(email, password, users)
                print(result)
                if result == "Вход выполнен успешно.":
                    break
            case "2":
                while True:
                    email = get_email()
                    if is_email_unique(email, users):
                        break
                    else:
                        print("Ошибка: Пользователь с таким email уже существует. Попробуйте еще раз.")

                password = get_password()
                password_confirm = get_password_confirm()
                if not are_passwords_match(password, password_confirm):
                    print("Ошибка: Пароли не совпадают.")
                    continue

                new_user = {"email": email, "password": password}
                users.append(new_user)

                with open('users.json', 'w', encoding='UTF-8') as write_users_to_file:
                    json.dump(users, write_users_to_file, indent = 4)

                print("Регистрация прошла успешно.")
            case "3":
                print('Программа завершена.')
                break
            case _:
                print("Неверный выбор. Попробуйте еще раз.")


if __name__ == '__main__':
    app()
