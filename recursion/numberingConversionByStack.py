class Stack:
    ''' Stack ADT implementation by list '''

    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)


def toStr(number, base):

    convertStr = '0123456789ABCDEF'

    s = Stack()

    while number > 0:
        if number < base:
            s.push(convertStr[number])
        else:
            s.push(convertStr[number % base])
        number //= base

    rs = ''
    while not s.isEmpty():
        rs += s.pop()

    return rs


print(toStr(1453, 16))
