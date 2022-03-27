from django.db import models
from colorama import init, Fore, Style


# модель пользователя
class User(models.Model):
    login = models.CharField(verbose_name="Имя", max_length=20)
    password = models.CharField(verbose_name="Пароль", max_length=20)
    online = models.BooleanField(verbose_name="Статус", default=False)

    def __str__(self):
        return f'{self.login} is {self.online}'


# модель чатов
class Chat(models.Model):
    user_name = models.CharField(verbose_name="Имя", max_length=20)
    chat_id = models.IntegerField(verbose_name="id_chat")
    users = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='chats')

    def __str__(self):
        return f'{self.chat_id}'

    # получить кто онлайн кто нет
    def get_online(self):
        chat = Chat.objects.exclude(user_name=self.user_name).get(chat_id=self.chat_id)
        if chat.users.online:
            return f'{Fore.GREEN + Style.BRIGHT}online'
        return f'{Fore.RED + Style.BRIGHT}offline'


# модель сообщений
class Messege(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=20)
    message = models.CharField(verbose_name="Сообщение", max_length=500)
    time_messege = models.DateTimeField(auto_now_add=True, blank=True)
    message_chat = models.ForeignKey(Chat, on_delete=models.CASCADE,
                                     related_name='chat_messages')

    def __str__(self):
        return f'Name: {self.name} -> Time: {self.time_messege}'

    # функция что бы вернуть время в нормальном виде
    def get_time(self):
        return f'{self.time_messege.strftime("%H:%M:%S, %d %B")}'
