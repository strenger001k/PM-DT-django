from calendar import c
import requests
from colorama import init, Fore, Style, Back
import time
import keyboard

init(autoreset=True)

after = 0

def print_message(message, name):
    print(Fore.GREEN + Style.BRIGHT + message['get_time'])
    if message['name'] == name:
        print(Fore.RED + Style.BRIGHT + message['name'])
    else:
        print(Fore.MAGENTA + Style.BRIGHT + message['name'])
    print(message['message'])
    print()



print(Fore.BLUE + Style.BRIGHT + "LOGIN")
login = input("Введите имя: ")
password = input("Введите пароль: ")
response = requests.post('http://127.0.0.1:8000/login', 
                        json= {
                            "name": login,
                            "pass": password
                        }
            )

if response.status_code != 404:
    print(Fore.BLUE + Style.BRIGHT + "login succeeded\n")
    chats = response.json()
    print("Hello " + Fore.RED + Style.BRIGHT + login + "!!!")

    choose = int(input('1. Create chat\n2. Open chat\n3. Exit\nChoose: '))
    while choose != 3:
        if choose == 1:
            username = input("Введите имя: ")
            requests.post('http://127.0.0.1:8000/chat', 
                            json= {
                                "name": username,
                                "login": login
                            }
            )

        elif choose == 2:
            if len(chats) != 0:
                for count, chat in enumerate(chats):
                    print(f"{count+1}. Chat with {Fore.CYAN + Style.BRIGHT}{chat['user_name']}")

                chat_number = int(input("Choose chat: "))
                while chat_number-1 >= len(chats):
                    print("Error")
                    chat_number = int(input("Choose chat: "))
                print()
                chat_id = chats[chat_number-1]['chat_id']
                chat_name = chats[chat_number-1]['user_name']

                while True:
                    response = requests.get('http://127.0.0.1:8000/messeges',
                                            params={'after': after, 'chat_id': chat_id, 'user_name': chat_name})
                    messages = response.json()
                    for message in messages:
                        print_message(message, login)
                        after = message['time_messege']
                    time.sleep(0.5)
                    if keyboard.is_pressed('ctrl'):
                        break
                print(Fore.BLUE + Style.BRIGHT + "EXIT")
            else:
                print("Chats are empty")

        choose = int(input('1. Create chat\n2. Open chat\n3. Exit\nChoose: '))
else:
    print(response.text)
