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
            self.last.next = Node(value, key)
            self.last = self.last.next
            self.length += 1

    def delem(self, key):
        s = 0
        current = self.head
        if current.key == key:
            self.head = current.next
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
    def __init__(self, _size = 10):




arr = LinkedList()
arr.addend(5, 'dog')
arr.addend(10, 'cat')
arr.addend(15, 'elephant')
arr.addend(25, 'your mama')
arr.addend(30, 'elephant')
arr.addend(29, 'elephant')
arr.addend(39, 'siu')

arr.delem('elephant')
print(arr)

