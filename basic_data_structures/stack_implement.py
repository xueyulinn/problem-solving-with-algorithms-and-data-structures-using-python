class Stack:
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


# class Stack:
#     def __init__(self) -> None:
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def peek(self):
#         if not self.isEmpty():
#             return self.items[0]

#     def push(self, val):
#         self.items.insert(0, val)

#     def pop(self):
#         if not self.isEmpty():
#             return self.items.pop(0)

#     def size(self):
#         return len(self.items)


# s = Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
