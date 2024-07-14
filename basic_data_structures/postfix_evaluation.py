from stack_implement import Stack


def postfixEval(postfixExpr):
    s = Stack()

    postfixList = postfixExpr.split()

    for i in postfixList:
        if i.isdigit():
            s.push(int(i))
        else:
            # an operator
            if not s.isEmpty():
                top2 = s.pop()
                top1 = s.pop()
                rs = doMath(i, top1, top2)
                s.push(rs)

    return s.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# print(postfixEval('7 8 + 3 2 + /'))


print(postfixEval('17 10 + 3 * 9 /'))

