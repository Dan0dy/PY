import random

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm       #打印速度
        self.currentTask = None   #打印任务
        self.timeRemaining = 0    #任务倒计时

    def tick(self):               #过去了一秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %(averageWait, printQueue.size()))

for i in range(10):
    print(simulation(3600, 5))
def hotPotato(namelist, num):
    simqueue = []
    for name in namelist:
        simqueue.insert(0, name)

    while len(simqueue) > 1:
        for i in range(num):
            simqueue.insert(0,simqueue[-1])
            simqueue.pop()
        simqueue.pop()
    return simqueue[-1]

def hotPotato2(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotPotato(['A','B','C','D','E','F'], 7))
print(hotPotato2(['A','B','C','D','E','F'], 7))
