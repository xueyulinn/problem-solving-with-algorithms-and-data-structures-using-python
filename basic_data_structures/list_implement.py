class Node:
    def __init__(self, val=0, next=None) -> None:
        self._val = val
        self._next = next

    def getData(self):
        return self._val

    def setData(self, val):
        self._val = val

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next


class UnorderedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, val):
        newNode = Node(val, self._head)
        self._head = newNode
        if self._tail is None:
            self._tail = newNode
        self._size += 1

    def remove(self, val):
        current = self._head
        previous = None

        while current is not None:
            if current.getData() == val:
                if previous is None:  # removing head
                    self._head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                if current == self._tail:  # removing tail
                    self._tail = previous
                self._size -= 1
                return True
            previous = current
            current = current.getNext()
        return False

    def append(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.setNext(newNode)
            self._tail = newNode
        self._size += 1

    def search(self, val):
        current = self._head
        while current is not None:
            if current.getData() == val:
                return True
            current = current.getNext()
        return False

    def index(self, val):
        current = self._head
        index = 0
        while current is not None:
            if current.getData() == val:
                return index
            index += 1
            current = current.getNext()
        return -1

    def insert(self, pos, val):
        if pos <= 0:
            self.add(val)
        elif pos >= self._size:
            self.append(val)
        else:
            newNode = Node(val)
            current = self._head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.getNext()
                index += 1
            newNode.setNext(current)
            previous.setNext(newNode)
            self._size += 1

    def pop(self):
        if self.isEmpty():
            return None
        current = self._head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        if previous is None:
            self._head = None
            self._tail = None
        else:
            previous.setNext(None)
            self._tail = previous
        self._size -= 1
        return current.getData()

    def pop_at(self, pos):
        if pos < 0 or pos >= self._size:
            return None
        if pos == 0:
            return self.remove_head()
        current = self._head
        previous = None
        index = 0
        while index < pos:
            previous = current
            current = current.getNext()
            index += 1
        previous.setNext(current.getNext())
        if current == self._tail:
            self._tail = previous
        self._size -= 1
        return current.getData()

    def remove_head(self):
        if self.isEmpty():
            return None
        current = self._head
        self._head = current.getNext()
        if self._head is None:
            self._tail = None
        self._size -= 1
        return current.getData()
