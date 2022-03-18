import requests
from colorama import init, Fore, Style
from sign_up import login_signup

init(autoreset=True)


user = login_signup()
if user:
    print(Fore.BLUE + Style.BRIGHT + "login succeeded\n")
    login = user['login']
    chats = user['chats']
    print("Hello " + Fore.RED + Style.BRIGHT + login + "!!!")

    if len(chats) != 0:
        for count, chat in enumerate(chats):
           print(f"{count+1}. Chat with {Fore.CYAN + Style.BRIGHT}{chat['user_name']}")

        chat_number = input("Choose chat: ")
        while not chat_number.isdigit():
            print("Enter integer numebr!!!")
            chat_number = input("Choose chat: ")
        chat_number = int(chat_number)

        while chat_number-1 >= len(chats):
            print("Error")
            chat_number = input("Choose chat: ")
            while not chat_number.isdigit():
                print("Enter integer numebr!!!")
                chat_number = input("Choose chat: ")
            chat_number = int(chat_number)
        print()
        chat_id = chats[chat_number-1]['chat_id']
        chat_name = chats[chat_number-1]['user_name']

        while True:
            text = input("Введите сообщение: ")
            requests.post('http://127.0.0.1:8000/messeges', 
                                json= {
                                    "name": login,
                                    "message": text,
                                    "chat_id": chat_id,
                                    "sender_name": chat_name
                                }
            )
else:
    print("By!")
