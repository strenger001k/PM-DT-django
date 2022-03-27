import requests
from sign_up import login_signup
from message import *
import time

user = login_signup()
if user:
    print(SUCCESSFUL_SIGNIN)
    login = user['login']
    password = user['password']
    chats = user['chats']
    print(HELLO_MESSAGE + login)

    if len(chats) != 0:
        print_chats(chats)
        chat_number = get_integer_value(CHOOSE_CHAT)
        while chat_number-1 >= len(chats):
            print(ERROR)
            chat_number = get_integer_value(CHOOSE_CHAT)
        print()
        username = chats[chat_number-1]['user_name']
        chat_id = chats[chat_number-1]['chat_id']
        chat_name = chats[chat_number-1]['user_name']

        print(CONSOL_QUIT)
        time.sleep(1.5)
        while True:
            text = input(GET_MESSAGE.format(username))
            if text == 'QUIT':
                break
            requests.post('http://127.0.0.1:8000/messeges',
                          json={
                                "name": login,
                                "message": text,
                                "chat_id": chat_id,
                                "sender_name": chat_name
                          })

        response = requests.post('http://127.0.0.1:8000/logout',
                                 json={
                                    "name": login,
                                    "pass": password
                                 })
else:
    print(EXIT)
