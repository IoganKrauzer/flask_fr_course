"""
Задача 1:
Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте потоки
"""

import requests
import threading
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://stepik.org/',
        'https://2.doramalive.news/',
        'https://pollen-attempt-4ac.notion.site/',
        'https://lnmtl.com/',
        'https://plati.market/'
        ]


def download(url):
    response = requests.get(url)
    dir_path = 'C:\\Users\Сергей\PycharmProjects\\flask_seminars\sem_4\\task_1_files\\'

    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    new_path = dir_path + filename
    with open(new_path, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


if __name__ == '__main__':
    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
