from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Сategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(verbose_name="Описание",
                                   max_length=300,
                                   blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')

    def __str__(self):
        return self.name


class Product(models.Model):
    card = models.ForeignKey(Сategory, null=True, default=None,
                             on_delete=models.CASCADE,
                             verbose_name="Карточка",
                             related_name='products')
    name = models.CharField(verbose_name="Название товара", max_length=20)
    description = models.CharField(verbose_name="Описание", max_length=300)
    scope = models.CharField(verbose_name="Сфера применения", max_length=300)
    diameter = models.FloatField(verbose_name="Диаметр", max_length=300)
    length = models.IntegerField(verbose_name="Длина")
    color = models.CharField(verbose_name="Цвет", max_length=300)
    photo = models.ImageField(verbose_name="Изображение",
                              upload_to='media/')

    def __str__(self):
        return f'{self.name}'

    def get_pic(self):
        return f'http://127.0.0.1:8000/media/{self.photo}'
