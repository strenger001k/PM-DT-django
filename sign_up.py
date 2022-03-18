from optparse import check_choice
import requests
from colorama import init, Fore, Style

init(autoreset=True)


def login_signup():
    choose = (input((f'1. {Fore.BLUE + Style.BRIGHT}SIGN IN\n{Style.RESET_ALL}'\
                     f'2. {Fore.BLUE + Style.BRIGHT}SIGN UP\n{Style.RESET_ALL}'\
                     f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                      'Choose: '))) 

    while not choose.isdigit():
        print("Enter integer numebr!!!")
        choose = (input((f'1. {Fore.BLUE + Style.BRIGHT}SIGN IN\n{Style.RESET_ALL}'\
                         f'2. {Fore.BLUE + Style.BRIGHT}SIGN UP\n{Style.RESET_ALL}'\
                         f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                          'Choose: ')))
    choose = int(choose)
    if choose == 1:
        print(Fore.BLUE + Style.BRIGHT + "LOGIN")
        login = input("login: ")
        password = input("pass: ")
        response = requests.post('http://127.0.0.1:8000/login', 
                                json= {
                                    "name": login,
                                    "pass": password
                                }
                    )
        while response.status_code == 404:
            print(Fore.RED + Style.BRIGHT + 'ERROR')
            login = input("login: ")
            password = input("pass: ")
            response = requests.post('http://127.0.0.1:8000/login', 
                                    json= {
                                        "name": login,
                                        "pass": password
                                    }
                        )

    elif choose == 2:
        print(Fore.BLUE + Style.BRIGHT + "SIGN UP")
        login = input("login: ")
        password = input("pass: ")
        response = requests.post('http://127.0.0.1:8000/signup', 
                                json= {
                                    "login": login,
                                    "password": password
                                }
                    )
        while response.status_code != 201:
            print(Fore.RED + Style.BRIGHT + 'LOGIN EXISTS')
            login = input("login: ")
            password = input("pass: ")
            response = requests.post('http://127.0.0.1:8000/signup', 
                                    json= {
                                        "login": login,
                                        "password": password
                                    }
                        )
        if response.status_code == 201:
            print('registration successful')
            response = requests.post('http://127.0.0.1:8000/login', 
                                json= {
                                    "name": login,
                                    "pass": password
                                }
                        )

    else:
        return

    return response.json()
