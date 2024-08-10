import os
from pathlib import Path
import argparse
import asyncio
import aiohttp
import time
from multiprocessing import Process
from threading import Thread
import requests

images_data = []
with open('./images/images.txt', 'r') as images:
    for image in images.readlines():
        images_data.append(image.strip())

PATH = Path('./images')


def download_img(url, dir_path=PATH):
    start_time = time.time()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(os.path.join(dir_path, filename), 'wb') as f:
        for data in response.iter_content(1024):
            f.write(data)
    print(f'Download: {filename} time spent: {time.time() - start_time:.2f} sec')


def download_img_thread(urls):
    threads = []
    start_time = time.time()

    for url in urls:
        thread = Thread(target=download_img, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Time spent: {time.time() - start_time:.2f} sec')


def download_img_process(urls):
    processes = []
    start_time = time.time()

    for url in urls:
        process = Process(target=download_img, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Time spent: {time.time() - start_time:.2f} sec')


async def download_img_async(urls):
    tasks = []
    start_time = time.time()

    for url in urls:
        task = asyncio.create_task(download_img_async(url))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print(f'Time spent: {time.time() - start_time:.2f} sec')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер изображений по URL-адресам')
    parser.add_argument('-u', '--urls', default=images_data, nargs='+', type=str,
                        help='Список URL-адресов для загрузки изображений')
    args = parser.parse_args()
    urls = args.urls

    print(f'Download {len(urls)} images. #Мультипотоки')
    download_img_thread(urls)
    print(f'Download {len(urls)} images. #Мультипроцессы')
    download_img_process(urls)
    print(f'Download {len(urls)} images. #Асинхронно')
    asyncio.run(download_img_async(urls))
