# Приложение для отрисовки древовидного меню 
#### (реализовано через templatetags)

### Установка и запуск приложения на локальном сервере

- установить все зависимости из пакета requirements.txt
```angular2html
pip install -r requirements.txt
```
- создать суперпользователя 'admin'
```angular2html
python manage.py createsuperuser
```
- выполнить миграции базы данных
```angular2html
python manage.py migrate
```
- запустить проект из папки с приложением
```angular2html
python manage.py runserver
```
- добавить через админ-панель "http://127.0.0.1:8000/admin/" в соответствующие модели пункты меню и по адресу "http://127.0.0.1:8000/" использовать добавленное меню.
- Меню можно использовать в любом шаблоне предварительно загрузив его:
```angular2html
{% load draw_menu %}

{% draw_menu 'имя_меню' %}
```