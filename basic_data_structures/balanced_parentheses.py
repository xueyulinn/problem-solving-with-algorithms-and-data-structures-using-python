from stack_implement import Stack


def parChecker(myStr):
    if myStr == '':
        return False

    s = []
    start_symbols = ['(', '[', '{']
    end_symbols = [')', ']', '}']

    for i in range(len(myStr)):
        if myStr[i] in start_symbols:
            s.append(myStr[i])
        elif myStr[i] in end_symbols:
            if s == []:
                return False
            s.pop()

    if (s == []):
        return True

    return False


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))
