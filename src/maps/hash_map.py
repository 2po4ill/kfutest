"""Модуль для создания Hash map."""

from src.maps.base_map import BaseMap


class Node:
    """ Класс для создания узла."""

    def __init__(self, value=None, next_node=None):
        self._value = value
        self.next = next_node

    def __str__(self):
        return f"Node(key={self.key}, value={self.value}"

    def __eq__(self, other):
        if self.key == other.key and self.value == other.value:
            return True
        return False

    def compare_value(self, value) -> bool:
        """ Сравнение значений. """

        return self._value == value


class LinkedList:
    """ Класс для создания односвязанного списка."""

    def __init__(self):
        self.head = None
        self.node = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            printed = '[' + str(self.head.value) + '(' + str(self.head.key) + ')'
            while self.head.next is not None:
                self.head = self.head.next
                printed += ',' + str(self.head.value) + '(' + str(self.head.key) + ')'
            return printed + ']'
        return '[None]'

    def back(self) -> Node:
        """ Вернуть последний узел списка. """

        if self.length != 0:
            node = self.head
            while node.next is not None:
                node = node.next
            return node
        raise IndexError("Список пустой.")

    def addend(self, value) -> None:
        """ Метод добавляющий узел в конец односвязного списка."""

        self.length += 1
        if not isinstance(value, Node):
            value = Node(value)
        if self.head is None:
            self.head = value
        else:
            self.back().next = value

    def del_head(self) -> None:
        """Удалить первый элемент списка."""

        self.head = self.head.next
        self.length -= 1

    def del_tail(self) -> None:
        """Удалить последний элемент списка."""

        if self.length == 1:
            self.head = None
            self.length -= 1
        elif self.length > 1:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None
            self.length -= 1

    def remove(self, value, for_all=False) -> None:
        """ Метод удаления узла из односвязного списка по ключу."""

        node = self.head
        if node.compare_data(value):
            self.del_head()
            if for_all is False:
                return
        while node.next.next is not None:
            if node.next.compare_data(value):
                node.next = node.next.next
                self.length -= 1
                if for_all is False:
                    return
            node = node.next
        if node.next.compare_data(value):
            node.next = node.next.next
            self.length -= 1

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        node = self.node
        if node is None:
            raise StopIteration
        self.node = self.node.next
        return node._value

    def __getitem__(self, item):
        if self.length >= item:
            node = self.head
            i = 0
            while i < item:
                node = node.next
                i += 1
            return node._value
        raise IndexError

    def __setitem__(self, key, value):
        if self.length >= key:
            node = self.head
            i = 0
            while i < key:
                node = node.next
                i += 1
            node._value = value


class HashMap(BaseMap):
    """ Класс для создания Hash map."""

    def __init__(self, _size=10):
        self._inner_list = LinkedList()
        for _ in range(_size):
            self._inner_list.addend(LinkedList())
        self._size = _size
        self._cnt = 0

    @property
    def inner_list(self):
        """ Список элементов. """

        return self._inner_list

    @property
    def cnt(self):
        """ Количество элементов хешмап. """

        return self._cnt

    def __getitem__(self, key):
        result = self._inner_list[hash(key) % self._size]
        if result.length == 0:
            raise KeyError("Ключ не найден.")
        for i in result:
            if i[0] == key:
                return i[1]
        raise KeyError("Ключ не найден.")

    def __setitem__(self, key, value):
        if self._inner_list[hash(key) % self._size].length == 0:
            self._cnt += 1
        flag = True
        for i in range(self._inner_list[hash(key) % self._size].length):
            if self._inner_list[hash(key) % self._size][i][0] == key:
                self._inner_list[hash(key) % self._size][i] = (key, value)
                flag = False
                break
        if flag:
            self._inner_list[hash(key) % self._size].addend((key, value))
            if self._cnt >= 0.8 * self._size:
                self._size *= 2
                new_inner_list = LinkedList()
                for _ in range(self._size):
                    new_inner_list.addend(LinkedList())
                for i in self._inner_list:
                    if i.length != 0:
                        for j in i:
                            new_inner_list[hash(j[0]) % self._size].addend(j)
                self._inner_list = new_inner_list
                new_cnt = 0
                for i in self._inner_list:
                    if i.length != 0:
                        new_cnt += 1
                self._cnt = new_cnt

    def __delitem__(self, key):
        deleted = self[key]
        self._inner_list[hash(key) % self._size].remove((key, deleted))
        if self._inner_list[hash(key) % self._size].length == 0:
            self._cnt -= 1

    def __len__(self):
        return self.__iter__().length

    def __iter__(self):
        temp = LinkedList()
        for i in self._inner_list:
            for j in i:
                temp.addend(j)
        return temp.__iter__()
