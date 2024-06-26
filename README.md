## Система аутентификации пользователей
Этот проект представляет собой простую систему аутентификации пользователей, реализованную на Python.<br>
Она позволяет пользователям регистрироваться и входить в систему, при этом пользовательские данные хранятся в файле JSON.

## Особенности
- Регистрация пользователя
- Подтверждение уникального адреса электронной почты
- Подтверждение пароля
- Постоянное хранение пользовательских данных в файле JSON

## Установка
1. Убедитесь, что в вашей системе установлен Python.
2. Клонировать репозиторий:
   ```
   https://github.com/kilona57/user-recognition-system
   ```
3. Создайте файл <b>users.json</b> в том же каталоге, что и другие файлы, если он еще не существует.

## Использование
1. Перейдите в каталог проекта в вашем терминале или командной строке.
2. Запустите следующую команду, чтобы запустить приложение:
   ```
   python app.py
   ```
3. Следуйте инструкциям на экране, чтобы зарегистрировать нового пользователя или войти в систему от имени существующего пользователя.

## Регистрация нового пользователя
1. Выберите опцию <b>"Регистрация"</b> в главном меню.
2. Введите уникальный адрес электронной почты.
3. Введите и подтвердите желаемый пароль.
4. Новый пользователь будет добавлен в файл <b>users.json</b>.

## Вход в систему
1. Выберите опцию <b>"Войти"</b> в главном меню.
2. Введите свой адрес электронной почты и пароль.
3. Если адрес электронной почты и пароль совпадают с именем существующего пользователя, вы успешно войдете в систему.

## Модули 
Проект состоит из следующих модулей:
1. <b>validators.py:</b>
    - Этот модуль содержит функции проверки, используемые во всем приложении.
    - Его цель - обеспечить централизованное размещение всей логики проверки, что делает код более модульным и простым в обслуживании.
2. <b>getters.py:</b>
    - Этот модуль содержит функции, отвечающие за запрос пользователя на ввод данных.
    - Он обеспечивает единый способ получения пользовательских данных, таких как адрес электронной почты и пароль, во всем приложении.
3. <b>app.py:</b>
    - Это основной файл приложения, который связывает все воедино.
    - Он импортирует функции из файлов <b>validators.py</b> и <b>getters.py</b> и использует их для реализации системы аутентификации пользователя.
    - Файл <b>app.py</b> отвечает за:
      - Отображение главного меню и обработку пользовательских настроек
      - Вызов соответствующих функций для регистрации нового пользователя или входа в систему существующего
      - Чтение из файла <b>users.json</b> и запись в него для хранения и извлечения пользовательских данных
## Функции
### <b>validators.py:</b>
1. <b>check_data(email: str, password: str, users: List[Dict[str, str]]) -> str:</b><br>
Проверяет, существуют ли пользователь с указанными email и password.
    - <b>Аргументы:</b>
      - email (str): Email пользователя.
      - password (str): Password пользователя.
      - users (List[Dict[str, str]]): Список существующих пользователей.
    - <b>Возвращает:</b>
      - str - Сообщение о результатах проверки.
2. <b>is_email_unique(email: str, users: List[Dict[str, str]]) -> bool:</b><br>
Проверяет, является ли email уникальным среди существующих пользователей.
    - <b>Аргументы:</b>
      - email (str): Email, который необходимо проверить.
      - users (List[Dict[str, str]]): Список существующих пользователей.
    - <b>Возвращает:</b>
      - bool - True, если email уникальный, False - если email уже существует.
3. <b>are_passwords_match(password: str, password_confirm: str) -> bool:</b><br>
Проверяет, совпадают ли введенный пароль и его подтверждение.
    - <b>Аргументы:</b>
      - password (str): Введенный пользователем пароль.
      - password_confirm (str): Введенное пользователем подтверждение пароля.
    - <b>Возвращает:</b>
      - bool - True, если пароли совпадают, False - если пароли не совпадают.
### <b>getters.py:</b>
1. <b>get_email() -> str:</b><br>
Запрашивает у пользователя ввод email.
    - <b>Возвращает:</b>
      - str - Введенный пользователем email.
2. <b>get_password() -> str:</b><br>
Запрашивает у пользователя ввод пароля.
    - <b>Возвращает:</b>
      - str - Введенный пользователем пароль.
3. <b>get_password_confirm() -> str:</b><br>
Запрашивает у пользователя подтверждение пароля.
    - <b>Возвращает:</b>
      - str - Введенное пользователем подтверждение пароля.
### <b>app.py:</b>
Файл <b>app.py</b> является основным приложением, которое использует функции из файлов <b>validators.py<b> и <b>getters.py</b>для реализации системы аутентификации пользователя.
Он предоставляет пользователям управляемый меню интерфейс для выбора между входом в систему, регистрацией и выходом. 
Пользовательские данные хранятся в файле </b>users.json</b>, который считывается и обновляется по мере необходимости.
1. <b>get_user_choice() -> str:</b><br>
Выводит меню выбора действий и запрашивает выбор пользователя.
    - <b>Возвращает:</b>
      - str - Выбранное пользователем действие.
2. app()
Основной цикл приложения, реализующий функциональность регистрации и входа.

## Зависимости
Этот проект не имеет каких-либо внешних зависимостей. В нем используются только встроенные модули Python.

## Способствование
Если вы обнаружите какие-либо проблемы или у вас есть предложения по улучшению, не стесняйтесь сообщать о проблеме или отправлять запрос на обновление.

## Лицензия
Этот проект лицензирован по лицензии MIT.

## Контакты
[github](https://github.com/kilona57)</br>
[gmail](kondrashka04@gmail.com)
