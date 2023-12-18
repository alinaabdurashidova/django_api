# Документация по проекту


## 1. Активация виртуального окружения

Виртуальное окружение создается в папке, где будет реализован проект. Далее необходимо набрать команды на терминале для создания и активации:

```
python3 -m venv venv

. venv/bin/activate
```

## 2. Установка расширений

Для установки сразу нескольких расширений создается текстовый файл **req.txt** и все их наименования прописываются в данном файле. Далее через терминал производится их установка по команде:

```
pip install -r req.txt
```


## 3. Создание базы данных

Для этого необходимо зайти через терминал в PostgreSql и создать базу данных по следующей команде:

```
CREATE DATABASE <Наименование базы данных>
```

(в данном проекте название БД - api_task)


## 4. Создание самого проекта

На терминале необходимо прописать следующую команду:

```
django-admin startproject config . 
```

После чего в папке нашего будет создан проект **config** со встроенными папками и файлами


## 5. Создания приложения ***Gadget***

Для создания новых приложений необходимо написать на терминале следующие команды:

```
python3 manage.py startapp Gadget

```

## 6. Загрузка приложения в файле settings.py

В данном файле необходимо добавить наши приложения в **INSTALLED_APPS**:
```python
INSTALLED_APPS = [
    ...
    'Gadget'
]
```

Также необходимо соединиться с базой данных, которую мы создали ранее:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'api_task',
        ...
        'HOST': 'localhost',
        'PORT':5432
    }
}

```
## 7. Создание моделей для приложения

Создание моделя для приложения **Gadget** в файле models.py (Gadget/models.py):

```python
from django.db import models

# Create your models here.

class Gadget(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.title} -> {self.pk}'
    
    
    class Meta:
        verbose_name = 'Гаджеты'
```

## 8. Миграции

Миграция является способом отслеживания изменений в структуре базы данных. В терминале необходимо будет прописать следующие команды:

```
python manage.py makemigrations
python manage.py migrate
```
## 9. Запуск сервера разработки Django

В термина прописываем следующую команду:

```
python3 manage.py runserver
```

Далее я работала в приложении **Postman** для запросов по url: http://localhost:8000/gadget/


### GET - вывод всех данных


http://localhost:8000/gadget/get/  - 

Вывод:

```
[
    {
        "id": 1,
        "title": "Sumsung S23",
        "price": 80000,
        "description": "multifunctional",
        "created_at": "2023-12-18"
    },
    {
        "id": 2,
        "title": "Sumsung S22",
        "price": 60000,
        "description": "new version",
        "created_at": "2023-12-18"
    }
]
```

### POST - создание новых данных

http://localhost:8000/gadget/create/  - 

Запрос:

title = Samsung S22

price = 60000

description = new version


Вывод:

```
{
    "id": 2,
    "title": "Sumsung S22",
    "price": 60000,
    "description": "new version",
    "created_at": "2023-12-18"
}
```

### GET - вывод данных по id

http://localhost:8000/gadget/get/1/

Вывод:

```
{
    "id": 1,
    "title": "Sumsung S23",
    "price": 80000,
    "description": "multifunctional",
    "created_at": "2023-12-18"
}
```

### PUT/PATCH - обновление существующих данных по id

http://localhost:8000/gadget/update/2/

Запрос:

title = Samsung S22 Plus

Вывод:

```
{
    "id": 2,
    "title": "Samsung S22 Plus",
    "price": 60000,
    "description": "new version",
    "created_at": "2023-12-18"
}
```

### DELETE - удаление данных по id

http://localhost:8000/gadget/delete/2/

Вывод:

DELETE /gadget/delete/2/ HTTP/1.1" 204 0