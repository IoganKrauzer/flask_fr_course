"""
Задача 3:
� Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход.
"""

import asyncio
import os

import aiohttp
import time

urls = [
    "https://www.google.ru/",
    "https://gb.ru/",
    "https://ya.ru/",
    "https://www.python.org/",
    "https://habr.com/ru/all/",
    "https://stepik.org/",
    "https://2.doramalive.news/",
    "https://pollen-attempt-4ac.notion.site/",
    "https://lnmtl.com/",
    "https://plati.market/",
]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
    dir_path = "C:\\Users\Сергей\PycharmProjects\\flask_seminars\sem_4\\task_3_files\\"
    filename = (
        "asyncio_"
        + url.replace("https://", "").replace(".", "_").replace("/", "")
        + ".html"
    )
    new_path = dir_path + filename
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


# async def main():
#     tasks = []
#     for url in urls:
#         task = asyncio.ensure_future(download(url))
#         tasks.append(task)
#         await asyncio.gather(*tasks)

# async def main():
#     tasks = []
#     for root, dirs, files in os.walk(PATH):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             tasks.append(asyncio.create_task(parser_url(file_path)))
#     await asyncio.gather(*tasks)


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == "__main__":
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
