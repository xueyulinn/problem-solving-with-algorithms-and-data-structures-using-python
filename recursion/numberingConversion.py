def toStr(number, base):
    convertStr = '0123456789ABCDEF'

    if number < base:
        return convertStr[number]
    else:
        return toStr(number//base, base) + convertStr[number % base]


print(toStr(1453, 16))
