from queue_implement import Queue


def hotPotato(nameList, num):
    q = Queue()

    for i in nameList:
        q.enqueue(i)

    while (q.size > 1):
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()
