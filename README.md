# Месенджер для бичей (<span style='color: SlateBlue;'>_beachgram_</span>)
### **Django REST framework**

* `menu.py` - Главное меню

    ![image alt](https://github.com/strenger001k/PM-DT-django/blob/messenger/readme_image/menu.png)

    После запуска вы сможете создать аккаунт или зайти в существующий.
    После успешного входа/регестрации вы попадете в главное меню и ваш статус для всех пользователей становится <span style='color: MediumSeaGreen;'>online</span>.

    В главном меню можно создать чат с тем или именным человеком, который прошел регестрацию.

    ![image alt](https://github.com/strenger001k/PM-DT-django/blob/messenger/readme_image/create_chat.png)

    Также можно зайти в существующий чат. Напротив каждого пользователй отображается его статус <span style='color: MediumSeaGreen;'>online</span>/<span style='color: Tomato;'>offline</span>. После того как вы зайдете в чат вы смоежете просматривать сообщения в реальном времени, что бы покинуть чат **удерживайте кнопку** `ALT`.

    ![image alt](https://github.com/strenger001k/PM-DT-django/blob/messenger/readme_image/open_chat.png)

    Что бы покинуть клеинт выбирете 3 пункт главного меню. Автоматически ваш статус будет <span style='color: Tomato;'>offline</span>.

    ![image alt](https://github.com/strenger001k/PM-DT-django/blob/messenger/readme_image/exit.png)


* `sender.py` - Клиент для отправки сообщений

**_продолжение будет_**

Запустить **ГЛАВНОЕ МЕНЮ** - `python menu.py`

Запустить **КЛИЕНТ ДЛЯ ОТПРАВКИ СООБЩЕНИЙ** - `python sender.py`