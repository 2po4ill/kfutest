"""Модуль для слияния файлов с подсчетом слов, создаваемых функцией wiki_parser"""


def merge(path1, path2, path):
    """ Объединить два файла в один. """

    with open(path, "w", encoding="utf-8") as result:
        with open(path1, "r", encoding="utf-8") as file1:
            with open(path2, "r", encoding="utf-8") as file2:
                line1 = file1.readline()
                line2 = file2.readline()
                count = 0
                while True:
                    if line1 == "" and line2 == "":  # Если два файла пустые
                        break

                    if line1 == "":  # Если один из файлов пустой
                        if count != 0:
                            line2 = "\n" + line2
                        while line2 != "":
                            result.write(line2)
                            line2 = file2.readline()
                        break

                    if line2 == "":  # Если один из файлов пустой
                        if count != 0:
                            line1 = "\n" + line1
                        while line1 != "":
                            result.write(line1)
                            line1 = file1.readline()
                        break

                    if line1.split()[0] < line2.split()[0]:  # Если не совпадение слов
                        result.write(line1)
                        line1 = file1.readline()
                        count = 1

                    elif line1.split()[0] > line2.split()[0]:  # Если не совпадение слов
                        result.write(line2)
                        line2 = file2.readline()
                        count = 1

                    else:  # Если совпадение слов
                        temp1 = line1.split()
                        temp2 = line2.split()
                        result.write(temp1[0] + ' ' + str(int(temp1[1]) + int(temp2[1])) + "\n")
                        line1 = file1.readline()
                        line2 = file2.readline()
                        count = 1


if __name__ == "__main__":
    merge(r'C:\Users\ydevl\PycharmProjects\kfutest\src\text\1.txt', r'C:\Users\ydevl\PycharmProjects\kfutest\src\text\2.txt', r'C:\Users\ydevl\PycharmProjects\kfutest\src\text\result.txt')
