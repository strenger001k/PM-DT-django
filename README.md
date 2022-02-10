# Тестовое задание
### PM Digital Transformation

Django project: <b>Магазин</b>

` pip install -r requirements.txt`

`python manage.py makemigrations main`

`python manage.py migrate`

`python manage.py runserver`

Список категорий - <code>http://127.0.0.1:8000/all_categories</code>

Список всех карточек товаров категории - <code>http://127.0.0.1:8000/all_objects</code>

Детальная информация о карточках - <code>http://127.0.0.1:8000/all_cards</code>

Для перехода на определенную карточку пропишите в адресной строке 
```
/card/pk
```
где pk номер нужной карточка

Пример: <code>http://127.0.0.1:8000/card/2</code>

Есть  <code><b>pk</b></code> под номером 2 и 3.<br>1 нету(

