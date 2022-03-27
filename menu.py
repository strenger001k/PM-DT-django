import requests
import time
import keyboard
from sign_up import login_signup
from message import *

after = 0


def get_new_chat(login, password): # функция для обновления чатов
    response = requests.post('http://127.0.0.1:8000/login', 
                        json= {
                            "name": login,
                            "pass": password
                        }
            )
    return response.json()['chats']


user = login_signup()
if user:
    print(SUCCESSFUL_SIGNIN)
    login = user['login']
    password = user['password']
    chats = user['chats']
    print(HELLO_MESSAGE + login)

    choose = get_integer_value(MAIN_MENU)
    while True:
        chats = get_new_chat(login, password)
        if choose == 1:
            all_users = requests.get('http://127.0.0.1:8000/login')
            all_users = all_users.json()

            all_users_name = [user['login'] for user in all_users if user['login'] != login]
            already_chat = []
            for user in all_users:
                if user['login'] == login:
                    for chat in user['chats']:
                        already_chat.append(chat['user_name'])
            print(LIST_USERS)
            print_user_name(all_users_name, already_chat)

            username = input(GET_NAME)
            create_chat = requests.post('http://127.0.0.1:8000/chat', 
                            json= {
                                "name": username,
                                "login": login
                            }
            )
            if create_chat.status_code == 404:
                print(ERROR)

        elif choose == 2:
            print_chats(chats)
            chat_number = get_integer_value(CHOOSE_CHAT)            
            while chat_number - 1 >= len(chats):
                print(ERROR)
                chat_number = get_integer_value(CHOOSE_CHAT) 

            print(KEYBOARD_ALT)
            time.sleep(1.5)

            chat_id = chats[chat_number-1]['chat_id']
            chat_name = chats[chat_number-1]['user_name']

            while True:
                response = requests.get('http://127.0.0.1:8000/messeges',
                                        params={'after': after,
                                                'chat_id': chat_id,
                                                'user_name': chat_name})
                messages = response.json()
                for message in messages:
                    print_message(message, login)
                    after = message['time_messege']
                time.sleep(0.5)

                if keyboard.is_pressed('alt'):
                    break
            print(EXIT)

        else:
            response = requests.post('http://127.0.0.1:8000/logout',
                        json= {
                            "name": login,
                            "pass": password
                        }
            )
            break
        choose = get_integer_value(MAIN_MENU)
else:
    print(EXIT)
