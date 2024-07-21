import turtle

def tree(branLen, t):
    if branLen > 5:
        t.forward(branLen)
        t.right(20)
        tree(branLen-15, t)
        t.left(40)
        tree(branLen-15, t)
        t.right(20)
        t.backward(branLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()

    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    myWin.exitonclick()


main()
