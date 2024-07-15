class Queue:
    ''' Queue ADT implementation by list '''
    def __init__(self) -> None:
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self):
        return self.items.pop()

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()