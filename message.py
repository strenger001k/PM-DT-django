from colorama import Fore, Style

SIGNUP_SIGNIN = f'1. {Fore.BLUE + Style.BRIGHT}SIGN IN\n{Style.RESET_ALL}'\
                f'2. {Fore.BLUE + Style.BRIGHT}SIGN UP\n{Style.RESET_ALL}'\
                f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
                 'Choose: '


MAIN_MENU = f'1. {Fore.BLUE + Style.BRIGHT}Create chat\n{Style.RESET_ALL}'\
            f'2. {Fore.GREEN + Style.BRIGHT}Open chat\n{Style.RESET_ALL}'\
            f'3. {Fore.RED + Style.BRIGHT}Exit\n{Style.RESET_ALL}'\
             'Choose: '


ERROR = Fore.RED + Style.BRIGHT + 'ERROR'
INTEGER_NUMBER = Fore.RED + Style.BRIGHT + 'ENTER INTEGER NUMEBR!!!'
EXIT = Fore.RED + Style.BRIGHT + 'EXIT'
KEYBOARD_ALT = Fore.RED + Style.BRIGHT + "press ALT to exit\n"


SIGNIN = Fore.BLUE + Style.BRIGHT + "SIGN IN"
SUCCESSFUL_SIGNIN = Fore.BLUE + Style.BRIGHT + '\nLOGIN SUCCEEDED\n'
SIGNUP = Fore.BLUE + Style.BRIGHT + "SIGN UP"
SUCCESSFUL_SIGNUP = Fore.BLUE + Style.BRIGHT + 'REGISTRATION SUCCESSFUL'
LOGIN_EXISTS = Fore.RED + Style.BRIGHT + 'LOGIN EXISTS'


HELLO_MESSAGE = "HELLO " + Fore.RED + Style.BRIGHT
LIST_USERS = Fore.GREEN + Style.BRIGHT + 'LIST OF USERS'
CHOOSE_CHAT = 'CHOOSE CHAT: '

GET_NAME = 'Enter name: '
GET_MESSAGE = 'Enter text: '
GER_LOGIN = 'login: '
GET_PASSWORD = 'pass: '


def get_integer_value(message):
    value = input(message)
    while not value.isdigit():
        print(INTEGER_NUMBER)
        value = input(message)
    return int(value)


def print_message(message, name):
    print(Fore.GREEN + Style.BRIGHT + message['get_time'])
    if message['name'] == name:
        print(Fore.RED + Style.BRIGHT + message['name'])
    else:
        print(Fore.MAGENTA + Style.BRIGHT + message['name'])
    print(message['message'])
    print()


def print_chats(chats):
    for count, chat in enumerate(chats):
        print(f"{count+1}. Chat with {Fore.CYAN + Style.BRIGHT}{chat['user_name']} "\
              f"{chat['get_online']}")


def print_user_name(all_users_name, already_chat):
    for name in all_users_name:
        if name not in already_chat:
            print(Fore.CYAN + Style.BRIGHT + name)
