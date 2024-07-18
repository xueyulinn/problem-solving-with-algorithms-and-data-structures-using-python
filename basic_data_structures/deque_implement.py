class Deque:
    def __init__(self) -> None:
        self.items = []

    def addFront(self, val):
        self.items.append(val)

    def removeFront(self):
        return self.items.pop()

    def addRear(self, val):
        self.items.insert(0, val)

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
