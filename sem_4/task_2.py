"""
Задача 2:
� Написать программу, которая считывает список из 10 URL адресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте процессы
"""
import multiprocessing
import requests
from multiprocessing import Process, pool
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
    dir_path = 'C:\\Users\Сергей\PycharmProjects\\flask_seminars\sem_4\\task_2_files\\'

    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    new_path = dir_path + filename
    with open(new_path, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

processes = []
start_time = time.time()

if __name__ == '__main__':


    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
