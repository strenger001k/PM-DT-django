import requests
from colorama import init, Fore, Style
import time
import keyboard
from sign_up import login_signup

init(autoreset=True)
after = 0


def get_new_chat(login, password): # функция для обновления чатов (если мы создали новый)
    response = requests.post('http://127.0.0.1:8000/login', 
                        json= {
                            "name": login,
                            "pass": password
                        }
            )
    return response.json()['chats']


def print_message(message, name):
    print(Fore.GREEN + Style.BRIGHT + message['get_time'])
    if message['name'] == name:
        print(Fore.RED + Style.BRIGHT + message['name'])
    else:
        print(Fore.MAGENTA + Style.BRIGHT + message['name'])
    print(message['message'])
    print()


user = login_signup()
if user:
    print(Fore.BLUE + Style.BRIGHT + "\nlogin succeeded\n")
    login = user['login']
    password = user['password']
    chats = user['chats']
    print("Hello " + Fore.RED + Style.BRIGHT + login + "!!!")

    choose = input((f'1. {Fore.BLUE + Style.BRIGHT}Create chat\n{Style.RESET_ALL}'\
                        f'2. {Fore.GREEN + Style.BRIGHT}Open chat\n{Style.RESET_ALL}'\
                        f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                         'Choose: '))
    while not choose.isdigit():
        print("Enter integer numebr!!!")
        choose = input((f'1. {Fore.BLUE + Style.BRIGHT}Create chat\n{Style.RESET_ALL}'\
                            f'2. {Fore.GREEN + Style.BRIGHT}Open chat\n{Style.RESET_ALL}'\
                            f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                             'Choose: '))
    choose = int(choose)
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
            print('list of users')
            for name in all_users_name:
                if name not in already_chat:
                    print(Fore.CYAN + Style.BRIGHT + name)

            username = input("Введите имя: ")
            create_chat = requests.post('http://127.0.0.1:8000/chat', 
                            json= {
                                "name": username,
                                "login": login
                            }
            )
            if create_chat.status_code == 404:
                print(Fore.RED + Style.BRIGHT + 'ERROR')

        elif choose == 2:
            for count, chat in enumerate(chats):
                print(f"{count+1}. Chat with {Fore.CYAN + Style.BRIGHT}{chat['user_name']} "\
                      f"{chat['get_online']}")

            chat_number = input("Choose chat: ")
            while not chat_number.isdigit():
                print("Enter integer numebr!!!")
                chat_number = input("Choose chat: ")
            chat_number = int(chat_number)
            
            while chat_number - 1 >= len(chats):
                print(Fore.RED + Style.BRIGHT + 'ERROR')
                chat_number = input("Choose chat: ")
                while not chat_number.isdigit():
                    print("Enter integer numebr!!!")
                    chat_number = input("Choose chat: ")
                chat_number = int(chat_number)

            print(Fore.RED + Style.BRIGHT + "press ALT to exit\n")
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
            print(Fore.BLUE + Style.BRIGHT + "EXIT")

        else:
            response = requests.post('http://127.0.0.1:8000/logout',
                        json= {
                            "name": login,
                            "pass": password
                        }
            )
            break

        choose = input((f'1. {Fore.BLUE + Style.BRIGHT}Create chat\n{Style.RESET_ALL}'\
                            f'2. {Fore.BLUE + Style.BRIGHT}Open chat\n{Style.RESET_ALL}'\
                            f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                             'Choose: '))
        while not choose.isdigit():
            print("Enter integer numebr!!!")
            choose = input((f'1. {Fore.BLUE + Style.BRIGHT}Create chat\n{Style.RESET_ALL}'\
                                f'2. {Fore.GREEN + Style.BRIGHT}Open chat\n{Style.RESET_ALL}'\
                                f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                                'Choose: '))
    choose = int(choose)
        
else:
    print("By!")
