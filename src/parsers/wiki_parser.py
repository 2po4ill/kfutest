"""Модуль для подсчета слов на странице вики."""

import os
import uuid
import re
import requests as req
import bs4 as bs
from src.maps.hash_map import HashMap


def wiki_parser(url: str, base_path):
    """Функция для подсчета слов на странице википедии и получении ссылок на встреченные слова"""

    base_path += "\\base_path"

    if os.path.exists(base_path):
        print("Папка уже существует.")
    else:
        os.mkdir(base_path)
        print("Папка создана.")

    booly = True
    dirlist = os.listdir(base_path)
    path = base_path
    for i in dirlist:
        with open(os.path.join(base_path, i, "url.txt"), "r", encoding="utf-8") as url_file:
            if url_file.read() == url:
                booly = False  # нашли url
                path = os.path.join(path, i)
                print("url уже был обработан")
                break
    print("url еще не был обработан")

    if booly:  # если url не нашли, тогда создаем url.txt и content.bin
        path = os.path.join(path, uuid.uuid4().hex)
        os.mkdir(path)
        with open(path + "\\url.txt", "w", encoding="utf-8") as url_file:
            url_file.write(url)
        text = req.request("GET", url).content
        with open(path + "\\content.bin", "wb") as content_file:
            content_file.write(text)

    with open(path + "\\content.bin", "rb") as content_file:
        soup = bs.BeautifulSoup(content_file, "lxml")
        hash_map = HashMap()
        for string in soup.stripped_strings:
            string = string.replace(".", "")
            string = string.replace(":", "")
            string = string.replace(";", "")
            string = string.replace(",", "")
            string = string.replace("«", "")
            string = string.replace("»", "")
            for word in string.split():
                if word[0] in r"""`~1234567890!@#$%^&*()-=_+[]{}\|/,.?'"№:;""":
                    continue
                try:
                    hash_map[word] += 1
                except KeyError:
                    hash_map[word] = 1
        hash_map.write(path + "\\words.txt")
        href_list = []
        for tag in soup.find_all(href=re.compile("^/wiki/")):
            href_list.append("https://ru.wikipedia.org" + tag["href"])
        return href_list


if __name__ == "__main__":
    result = wiki_parser('https://en.wikipedia.org/wiki/B-tree#Insertion', r'A:\jkjkjkjk')
    for j in result:
        print(j)
