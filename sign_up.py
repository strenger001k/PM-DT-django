import requests
from colorama import init, Fore, Style
from message import *

init(autoreset=True)


def login_signup():
    choose = get_integer_value(SIGNUP_SIGNIN)
    if choose == 1:
        print(SIGNIN)
        login = input(GER_LOGIN)
        password = input(GET_PASSWORD)
        response = requests.post('http://127.0.0.1:8000/login', 
                                json= {
                                    "name": login,
                                    "pass": password
                                }
                    )
        while response.status_code == 404:
            print(ERROR)
            login = input(GER_LOGIN)
            password = input(GET_PASSWORD)
            response = requests.post('http://127.0.0.1:8000/login', 
                                    json= {
                                        "name": login,
                                        "pass": password
                                    }
                        )

    elif choose == 2:
        print(SIGNUP)
        login = input(GER_LOGIN)
        password = input(GET_PASSWORD)
        response = requests.post('http://127.0.0.1:8000/signup', 
                                json= {
                                    "login": login,
                                    "password": password
                                }
                    )
        while response.status_code != 201:
            print(LOGIN_EXISTS)
            login = input(GER_LOGIN)
            password = input(GET_PASSWORD)
            response = requests.post('http://127.0.0.1:8000/signup', 
                                    json= {
                                        "login": login,
                                        "password": password
                                    }
                        )
        if response.status_code == 201:
            print(SUCCESSFUL_SIGNUP)
            response = requests.post('http://127.0.0.1:8000/login', 
                                json= {
                                    "name": login,
                                    "pass": password
                                }
                        )

    else:
        return

    return response.json()
