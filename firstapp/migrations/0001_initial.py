# Generated by Django 4.0.2 on 2022-02-10 19:28

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Сategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Описание')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='firstapp.сategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название товара')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('scope', models.CharField(max_length=300, verbose_name='Сфера применения')),
                ('diameter', models.FloatField(max_length=300, verbose_name='Диаметр')),
                ('length', models.IntegerField(verbose_name='Длина')),
                ('color', models.CharField(max_length=300, verbose_name='Цвет')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Изображение')),
                ('card', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='firstapp.сategory', verbose_name='Карточка')),
            ],
        ),
    ]
