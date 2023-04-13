import json
import os
import socket
from django.http import HttpResponse, JsonResponse


def json_files_view(request):
    # Определяем путь к папке с json-файлами
    path = "C:\Project\Django\HW\15.12\json"

    # Получаем список файлов в папке
    files = os.listdir(path)

    # Создаем сокет для передачи данных на сервер
    s = socket.socket()
    host = 'localhost'
    port = 5432
    s.connect((host, port))

    # Читаем каждый файл и отправляем на сервер
    for file_name in files:
        if file_name.endswith('.json'):
            file_path = os.path.join(path, file_name)
            with open(file_path) as f:
                data = json.load(f)
                s.send(json.dumps(data).encode())

            # Получаем ответ от сервера и записываем его в файл
            response = s.recv(1024).decode()
            with open(file_path, 'w') as f:
                f.write(response)

    s.close()

    # Возвращаем ответ на запрос
    return HttpResponse('Json files updated.')
