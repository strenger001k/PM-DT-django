from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=20)
    message = models.CharField(verbose_name="Сообщение", max_length=20)

    def __str__(self):
        return f'{self.name}'
