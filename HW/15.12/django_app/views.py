import os
import json
import socket
import threading


def process_data(data):
    for item in data['data']:
        item['processed_by'] = 'view.py'
        if 'unwanted_key' in item:
            del item['unwanted_key']
    return data


def start_server():
    # Создаем сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        # Ожидаем соединения
        print('Ожидание соединения...')
        connection, client_address = sock.accept()

        try:
            print('Получено подключение от', client_address)

            # Получаем список файлов
            files = os.listdir()

            # Отправляем каждый файл на сервер
            for file_name in files:
                if file_name.endswith('.json'):
                    with open(file_name, 'r') as f:
                        data = json.load(f)
                        json_data = json.dumps(data)

                        # отправляем данные на сервер
                        connection.sendall(json_data.encode('utf-8'))

                        # ответ от сервера
                        received_data = connection.recv(1024).decode('utf-8')
                        received_data = json.loads(received_data)

                        with open(file_name, 'w') as f:
                            json.dump(received_data, f)

        finally:

            connection.close()


def start_client():
    # Создаем сокет и подключаемся к серверу
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)
    sock.connect(server_address)

    try:
        while True:
            # Получаем данные от сервера
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break

            # Обрабатываем данные
            received_data = json.loads(data)
            processed_data = process_data(received_data)

            # Отправляем обработанные данные обратно на сервер
            json_data = json.dumps(processed_data)
            sock.sendall(json_data.encode('utf-8'))
    finally:
        sock.close()


if __name__ == '__main__':
    start_server()

    client_thread = threading.Thread(target=start_client)
    client_thread.start()

# import json
# import os
# import socket
# from django.http import HttpResponse, JsonResponse
#
#
# def json_files_view(request):
#     # Определяем путь к папке с json-файлами
#     path = "C:\Project\Django\HW\15.12\json"
#
#     # Получаем список файлов в папке
#     files = os.listdir(path)
#
#     # Создаем сокет для передачи данных на сервер
#     s = socket.socket()
#     host = 'localhost'
#     port = 5432
#     s.connect((host, port))
#
#     # Читаем каждый файл и отправляем на сервер
#     for file_name in files:
#         if file_name.endswith('.json'):
#             file_path = os.path.join(path, file_name)
#             with open(file_path) as f:
#                 data = json.load(f)
#                 s.send(json.dumps(data).encode())
#
#             # Получаем ответ от сервера и записываем его в файл
#             response = s.recv(1024).decode()
#             with open(file_path, 'w') as f:
#                 f.write(response)
#
#     s.close()
#
#     # Возвращаем ответ на запрос
#     return HttpResponse('Json files updated.')
