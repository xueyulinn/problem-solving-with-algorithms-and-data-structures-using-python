from queue_implement import Queue
import random

class Printer:
    def __init__(self, ppm) -> None:
        self.remainingTime = 0
        self.currentTask = None
        self.ppm = ppm

    def isBusy(self):
        return self.currentTask != None

    def tick(self):
        if self.remainingTime > 0:
            self.remainingTime -= 1
        else:
            self.currentTask = None

    def startNext(self, task):
        self.currentTask = task
        self.remainingTime = task.getPage() * 60 / self.ppm


class Task:
    def __init__(self, page, createdTime) -> None:
        self.page = page
        self.createdTime = createdTime

    def getPage(self):
        return self.page

    def getCreatedTime(self):
        return self.getCreatedTime

    def waitTime(self, currentTime):
        return currentTime - self.createdTime


def simulation(ppm, seconds):
    waitings = []
    printTask = Queue()
    labPrinter = Printer(ppm)

    for currentSecond in range(seconds):
        if newTask() == True:
            task = Task(random.randrange(1, 21), currentSecond)
            printTask.enqueue(task)

        else:
            if (not printTask.isEmpty()) and (not labPrinter.isBusy()):
                task = printTask.dequeue()
                waitings.append(task.waitTime(currentSecond))
                labPrinter.startNext(task)

        labPrinter.tick()

    if waitings:
        averageWait = sum(waitings)/len(waitings)
    else:
        averageWait = 0

    print(f'In {seconds} seconds {len(waitings)} tasks were created, avgerage waiting time is {averageWait} s task reamining: {printTask.size()} ')


def newTask():
    if random.randrange(1, 181) == 180:
        return True
    else:
        return False


simulation(10, 3600)
