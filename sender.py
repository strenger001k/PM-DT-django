import requests

name = input("Введите имя: ")
while True:
    text = input("Введите сообщение: ")
    requests.post('http://127.0.0.1:8000/users', 
                        json= {
                            "name": name,
                            "message": text
                        }
    )
