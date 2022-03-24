class Node:
    def __init__(self, value, key, next = None):
        self.value = value
        self.key = key
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            llstr = '[' + str(self.head.value) + '(' + str(self.head.key) + ')'
            while self.head.next is not None:
                self.head=self.head.next
                llstr += ',' + str(self.head.value) + '(' + str(self.head.key) + ')'
            return llstr + ']'
        return '[None]'

    def addend(self, value, key):
        if self.head is None:
            self.head = Node(value, key)
            self.last = self.head
            self.length += 1
        else:
            current = self.head
            while current is not None:
                if current.key == key:
                    current.value = value  #заменяем значение если есть уже похожий ключ
                    return
                current = current.next
            self.last.next = Node(value, key)
            self.last = self.last.next
            self.length += 1

    def delem(self, key):
        s = 0
        current = self.head
        if current.key == key:
            self.head = self.head.next
            self.length -= 1
        else:
            while current.next is not None:
                if current.next.key == key:
                    if current.next.next is None:
                        current.next = None
                    else:
                        current.next = current.next.next
                    self.length -= 1
                    s += 1
                if current.next is not None and current.next.key != key:
                    current = current.next
                else:
                    if current.next.next is not None:
                        current.next = current.next.next
                    else:
                        current.next = None
        if s != 0:
            return
        else:
            return print('wrong key, try again')

class HashMap:
    def __init__(self, size = 10):
        self._inner_list = [None] * size
        self._size = size
        self._ctr = 0  #counter

    def __getitem__(self, key):
        linkedlist = self._inner_list[hash(key) % self._size]  #получаем связанный список из заданной ячейки хэшмапы
        if linkedlist is None:
            return print('wrong key')
        while linkedlist.head is not None:
            if linkedlist.head.key == key:
                return linkedlist.head.value
            linkedlist = linkedlist.next
        return None

    def __setitem__(self, key, value):
        adress = hash(key) % self._size
        if self._inner_list[adress] is None:
            self._inner_list[adress] = LinkedList()
            self._inner_list[adress].addend(value, key)  #засовываем в пустую ячейку хэшмапы связанный список с ключом и value
        else:
            while self._inner_list[adress].head is not None:
                if self._inner_list[adress].head.key == key:
                    self._inner_list[adress].head.value = value  #ищем узел с похожим ключом и меняем значение
                    return
                self._inner_list[adress].head = self._inner_list[adress].head.next
            self._inner_list[adress].addend(value, key)
        self._ctr += 1
        if self._ctr >= 0.8 * self._size:
            self._size = self._size * 2 #при увеличении счетчика ключей/значений надо увеличивать размер мапы
            new_list = [None] * self._size
            for _ in self._inner_list:
                if _ is not None:
                    while _.head is not None:
                        adress = hash(_.head.key) % self._size
                        if new_list[adress] is None:
                            new_list[adress] = LinkedList()
                            new_list[adress].addend(_.head.key, _.head.value)  #заново перераспределяем ключи/значения
                        else:
                            new_list[adress].addend(_.head.key, _.head.value)
                        _.head = _.head.next
            self._inner_list = new_list

    def __delitem__(self, key):
        booly = 0
        for linkedlist in self._inner_list:
            if linkedlist is not None:
                lengthcheck = linkedlist.length
                linkedlist.delem(key)
                if linkedlist.length != lengthcheck:
                    booly = 1
                    break;
        if booly == 1:
            self._cnt -= 1
            if self._size * 0.8 > self._ctr and self._size > 10:
                self._size = self._size // 2
                new_list = [None] * self._size
                for _ in self._inner_list:
                    if _ is not None:
                        while _.head is not None:
                            adress = hash(_.head.key) % self._size
                            if new_list[adress] is None:
                                new_list[adress] = LinkedList()
                                new_list[adress].addend(_.head.key, _.head.value)  # заново перераспределяем ключи/значения
                            else:
                                new_list[adress].addend(_.head.key, _.head.value)
                            _.head = _.head.next
                self._inner_list = new_list
        else:
            return print('wrong key')


arr = LinkedList()


arr.addend(15, 'elephant')

arr.addend(30, 'elephant')
arr.addend(31, 'elephant')
arr.delem('elephant')


print(arr)

