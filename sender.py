import requests
from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.BLUE + Style.BRIGHT + "LOGIN")
name = input("Введите имя: ")
password = input("Введите пароль: ")
response = requests.post('http://127.0.0.1:8000/login', 
                        json= {
                            "name": name,
                            "pass": password
                        }
            )

if response.status_code != 404:
    print(Fore.BLUE + Style.BRIGHT + "login succeeded\n")
    chats = response.json()
    print("Hello " + Fore.RED + Style.BRIGHT + name + "!!!")

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
            text = input("Введите сообщение: ")
            requests.post('http://127.0.0.1:8000/messeges', 
                                json= {
                                    "name": name,
                                    "message": text,
                                    "chat_id": chat_id,
                                    "sender_name": chat_name
                                }
            )
else:
    print(response.text)