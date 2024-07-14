from stack_implement import Stack


def baseConverter(number, base):
    str = '0123456789ABCDEF'
    s = Stack()

    while number > 0:
        rem = number % base
        s.push(str[rem])
        number = number // base

    rs = ''
    while not s.isEmpty():
        rs += s.pop()

    return rs


print(baseConverter(25, 8))
print(baseConverter(256, 16))
print(baseConverter(26, 26))
