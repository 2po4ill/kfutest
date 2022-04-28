"""Модуль для подсчета слов на странице вики."""

import os
import uuid
import re
from src.maps.hash_map import HashMap


def wiki_parser(url: str, base_path: str) -> HashMap:
    """Функция для подсчета слов на странице википедии."""

    if os.path.exists:
        print("Папка уже существует.")
    else:
        os.mkdir(base_path)
        print("Папка создана.")

    bool = True
    dirlist = os.listdir(base_path)
    path = base_path
    for i in dirlist:
        with open(os.path.join(base_path, i, "url.txt"), "r", encoding="utf-8") as url_file:
            if url_file.read() == url:
                bool = False #нашли url
                path += "\\" + i
                path = os.path.join(path, i)
                print("url уже был обработан")
                break
    print("url еще не был обработан")

    if bool: #если url не нашли, тогда создаем url.txt и content.bin
        path = os.path.join(path, uuid.uuid4().hex)
        os.mkdir(path)
        text = req.request("GET", url).content
        with open(path + "\\content.bin", "wb") as content_file:
            content_file.write(text)
        with open(path + "\\url.txt", "w", encoding="utf-8") as url_file:
            url_file.write(url)

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
        href_list = HashMap()
        i = 0
        for tag in soup.find_all(href=re.compile("^/wiki/")):
            href_list[i] = tag["href"]
            i += 1
            return href_list


if __name__ == "__main__":
    wiki_parser('https://ru.wikipedia.org/wiki/Чёрмозский_завод',
                r'A:\jkjkjkjk')