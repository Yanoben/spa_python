# spa_python
SPA with Python

### Запуск проекта в dev-режиме
- Сначала клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Yanoben/spa_python
```

- Установите и активируйте виртуальное окружение
```
python -m venv venv

. venv/bin/activate
```

- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 

- В папке с файлом manage.py выполните команду:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
