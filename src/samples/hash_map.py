from typing import Iterable, Tuple
from src.maps.base_map import BaseMap


class HashMap(BaseMap):
    """A class to represent HashMap data structur e"""
    class Node:

        def __init__(self, value, key, next_node=None):
            self.value = value
            self.key = key  # key for dictionary is stored here
            self.next = next_node

        def __iter__(self) -> Iterable[Tuple[str, int]]:
            yield self.key, self.value

            if self.next is not None:
                yield from self.next

        def __str__(self):
            return f"key: {self.key}, value: {self.value}"

    # Linked list`s class
    class LinkedList:
        """A class to represent LinkedList data structure"""
        def __init__(self):
            self.head = None
            self.end = None
            self.length = 0

        def insert_at_end(self, value, key):
            """Method that inserts a node at the end of LinkedList"""
            if self.head is None:
                self.head = self.end = HashMap.Node(value, key)
            else:
                self.end.next = self.end = HashMap.Node(value, key)
            self.length += 1

        def delete_by_key(self, key):
            """Method that deletes node from LinkedList by key"""
            current = self.head
            if self.head.key == key:
                self.head = self.head.next
            else:
                while current.next is not None:
                    if current.next.key == key:
                        current.next = current.next.next
                        self.length -= 1
                        break

        def __len__(self):
            return self.length

        # method for formatting LinkedList
        def __str__(self):
            if self.head is not None:
                current = self.head
                result = f'[{current.value}, '
                while current.next is not None:
                    current = current.next
                    result += f'{current.value}, '
                result = result[:-2]
                result += ']'
                return result
            return '[]'

        def __iter__(self) -> Iterable[Tuple[str, int]]:
            if self.head is not None:
                yield from self.head

    # initializing dictionary
    def __init__(self, size=10):
        self._inner_list = [None] * 10
        self._size = size  # attribute to store length
        self._cnt = 0   # attribute to store how many elements were added

    def __iter__(self) -> Iterable[Tuple[str, int]]:
        for linklist in self._inner_list:
            yield from linklist or []

    # getting item by key
    def __getitem__(self, key):
        linklist = self._inner_list[hash(key) % self._size]
        if linklist is None:
            raise KeyError('No element with such key')
        current = linklist.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError('No element with such key')

    # setting element by magic method
    def __setitem__(self, key, value):
        index = hash(key) % self._size
        if self._inner_list[index] is None:
            self._inner_list[index] = HashMap.LinkedList()
            self._inner_list[index].insert_at_end(value, key)
        else:
            lst = self._inner_list[index]
            current = lst.head
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            lst.insert_at_end(value, key)
        self._cnt += 1
        # if number of elements in dict is 80% of size, increasing size
        if self._cnt >= 0.8 * self._size:
            self._size = self._size * 17 // 10  # increasing by 1.7 to make more random indexes
            new_inner_list = [None] * self._size
            for linlist in self._inner_list:
                if linlist is not None:
                    current = linlist.head
                    while current is not None:
                        index = hash(current.key) % self._size
                        if new_inner_list[index] is None:
                            new_inner_list[index] = HashMap.LinkedList()
                            new_inner_list[index].insert_at_end(current.value, current.key)
                        else:
                            lst = new_inner_list[index]
                            lst.insert_at_end(current.key, current.value)
                            # while curr is not None:
                            #     if curr.key == key:
                            #         curr.value = value
                            #         return
                            #     curr = curr.next
                            # lst.insert_at_end(value, key)
                        current = current.next
            self._inner_list = new_inner_list

    # deleting element of HashMap by key and making HashMap smaller is necessary
    def __delitem__(self, key):
        for linklist in self._inner_list:
            if linklist is not None:
                linklist.delete_by_key(key)
        self._cnt -= 1
        if self._size * 0.8 > self._cnt and self._size > 10:
            self._size = self._size // 17 * 10  # decreasing by 2
            new_inner_list = [None] * self._size
            for linlist in self._inner_list:
                if linlist is not None:
                    current = linlist.head
                    while current is not None:
                        index = hash(current.key) % self._size
                        if new_inner_list[index] is None:
                            new_inner_list[index] = HashMap.LinkedList()
                            new_inner_list[index].insert_at_end(current.value, current.key)
                        else:
                            lst = new_inner_list[index]
                            lst.insert_at_end(current.value, current.key)
                        current = current.next
            self._inner_list = new_inner_list

    def __len__(self):
        return self._cnt

    def __str__(self):
        return '[' + ', '.join(map(str, self._inner_list)) + ']'


if __name__ == "__main__":
    hm = HashMap()
    for i in range(10):
        hm[i] = i
    del hm[3]
    list_map = list(hm)
    print(list_map)