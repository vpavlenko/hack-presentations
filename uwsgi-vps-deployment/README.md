Как задеплоить Flask через uWSGI на VPS-сервер
==============================================

[Flask](http://flask.pocoo.org/) - легкий веб-фреймворк на Питоне.

[Отличный туториал по связке nginx - uWSGI - Django](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html)



Установка
---------

- Ставим Flask:
```sh
# apt-get install python-setuptools
# easy_install-2.7 pip
# pip install flask
```

- Ставим uWSGI:
```sh
# apt-get install python-dev gcc   # uwsgi содержит Python/C interaction
# pip install uwsgi
```

- Ставим nginx:
```sh
# apt-get install nginx
```


Конфигурация
------------

Конфиг nginx лежит в `/etc/nginx/sites-enabled/default`.

Пусть мы хотим отдавать во flask-приложение всё, что приходит на домен
`my_vps_server.com/flask/`.

Будем дружить uWSGI и nginx через TCP-порты.

Допишем в [конфиг nginx](default):
```conf
location ~* /flask { try_files $uri @flask; }
location @flask {
  rewrite ^/flask(.*) $1 break;
  include uwsgi_params;
  uwsgi_pass 127.0.0.1:9090;
}
```

Вот наше простейшее [flask-приложение](flaskhello.py):
```python
from flask import Flask
app = Flask(__name__)

@app.route('/<address>')
def hello_world(address):
    return 'Hello World! Called with ' + address
```

Запустим uWSGI командой
```sh
su - www-data -c "uwsgi --socket 127.0.0.1:9090 --wsgi-file /usr/share/nginx/www/flaskhello.py --callable app&"
```


Таски
-----

1. Научиться напрямую сёрвить директории файлов через nginx (managing static files). Просто отдавать файлы из конкретной папки.

2. Дочитать подвал [статьи про Django - uWSGI - nginx](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html), попробоваь сделать фишки из него.

3. Научиться деплоиться, выкачивая код из репозитория. См. [Capistrano](http://habrahabr.ru/post/49127/). Положить код Summarization в svn/git.