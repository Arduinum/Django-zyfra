import urllib.parse


form = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>\
    <form method="post"><h1>Форма для имени</h1><input type="text" \
    placeholder="введите имя" name="name" ><button type="submit">Сохранить\
    </button></form></body></html>'

def application(env, start_response):
    path = env.get('PATH_INFO', '/')

    if path == '/':
        start_response('200 OK', [('Content-Type','text/html')])
        return [b'Hello World']
    elif path == '/about':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"it's me"]
    elif path == '/say_hello':
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        name = env['wsgi.input'].read()
        print(name)
        if name:
            name_code_url = name.decode("utf-8").split('=')[1]
            name = urllib.parse.unquote(name_code_url)
            answer = f'«Привет, {name}»'
            return [answer.encode('utf-8')]
        return [form.encode('utf-8')]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [b'Page not found!']

# старт сервера с настройками:
# uwsgi --http-socket 127.0.0.1:8080 --ini router.ini --wsgi-file router.py
