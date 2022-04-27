"""Модуль для создания Hash map."""

from src.maps.base_map import BaseMap


class Node:
    """ Класс для создания узла."""

    def __init__(self, value, key, next=None):
        self.value = value
        self.next = next
        self.key = key

    def __str__(self):
        return f"Node(key={self.key}, value={self.value}"

    def __eq__(self, other):
        if self.key == other.key and self.value == other.value:
            return True
        return False


class LinkedList:
    """ Класс для создания односвязанного списка."""

    def __init__(self):
        self.head = None
        self.back = None
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

    def addend(self, value, key):
        """ Метод добавляющий узел в конец односвязного списка."""

        if self.head is None:
            self.head = Node(value, key)
            self.back = self.head
            self.length += 1
        else:
            current = self.head
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            self.back.next = Node(value, key)
            self.back = self.back.next
            self.length += 1

    def delem(self, key):
        """ Метод удаления узла из односвязного списка по ключу."""

        current = self.head
        if current.key == key:
            self.head = self.head.next
            self.length -= 1
        else:
            while current.next is not None:
                if current.next.key == key:
                    current.next = current.next.next
                    self.length -= 1
                    return
                current = current.next

    def __iter__(self):
        self.node = self.head
        return self


class HashMap(BaseMap):
    """ Класс для создания Hash map."""

    def __init__(self, _size=10):
        self._size = _size
        self._count = 0
        self._inner_list = [LinkedList()] * _size

    def __getitem__(self, key):
        nod = self._inner_list[hash(key) % self._size].head
        while nod is not None:
            if nod.key == key:
                return nod.value
            nod = nod.next
        return print('wrong key')

    def __setitem__(self, key, value):
        nod = self._inner_list[hash(key) % self._size].head
        booly = 0
        while nod is not None:
            if nod.key == key:
                nod.value = value
                booly = 1
                break
            nod = nod.next
        if booly == 0:
            self._inner_list[hash(key) % self._size].addend(value, key)
            self._count += 1
        if self._count >= 0.8 * self._size:
            self._size = self._size * 2
            new_inner_list = [LinkedList()] * self._size
            for linkedlist in self._inner_list:
                node1 = linkedlist.head
                while node1 is not Node:
                    new_inner_list[hash(node1.key) % self._size].addend(node1.value, node1.key)
                    node1 = node1.next
            self._inner_list = new_inner_list

    def __delitem__(self, key):
        linkedlist = self._inner_list[hash(key) % self._size]
        linkedlist.delem(key)
        self._count -= 1
        if self._count < 0.8 * self._size:
            self._size = self._size // 2
            new_inner_list = [LinkedList()] * self._size
            for linkedlist in self._inner_list:
                node2 = linkedlist.head
                while node2 is not None:
                    new_inner_list[hash(node2.key) % self._size].addend(node2.value, node2.key)
                    node2 = node2.next
            self._inner_list = new_inner_list

    def __str__(self):
        printed = ''
        for linkedlist in self._inner_list:
            printed += str(linkedlist) + '\n'
        return printed

    def __iter__(self):
        temp = LinkedList()
        for i in self._inner_list:
            for j in i:
                temp.addend(j)
        return temp.__iter__()

    def __len__(self):
        return self.__iter__().length
