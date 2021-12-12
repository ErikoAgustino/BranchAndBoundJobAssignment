class Node:
    def __init__(self, n, worker, job, cost, assigned, parent):
        self.parent = parent
        self.worker = worker
        self.job = job
        self.cost = cost

        self.assigned = [False] * n
        for x in range(n):
            self.assigned[x] = assigned[x]

        if(parent != None):
            self.cost += parent.getCost()

        if(job > -1):
            self.setAssignedValue(True, job)

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setWorker(self, worker):
        self.worker = worker

    def getWorker(self):
        return self.worker

    def setJob(self, job):
        self.job = job

    def getJob(self):
        return self.job

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost

    def setAssignedValue(self, value, index):
        self.assigned[index] = value

    def getAssignedValue(self, index):
        return self.assigned[index]

    def getAssigned(self):
        return self.assigned

    def PrintOut(self):
        print("Parent:", self.getParent())
        print("Worker:", self.getWorker())
        print("Job:", self.getJob())
        print("Cost:", self.getCost())
        print("Assigned:", self.getAssigned())
        print()


def Main():
    n = 4
    costMatrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
    #costMatrix = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]
    # costMatrix = [[10, 12, 19, 11], [5, 10, 7, 8],[12, 14, 13, 11], [8, 15, 11, 9]]
    assignedArr = [False] * n

    childArr = []

    # parent
    parent = Node(n, -1, -1, 0, assignedArr, None)
    for x in range(n):
        child = Node(n, parent.getWorker() + 1, x,
                     costMatrix[parent.getWorker() + 1][x], parent.getAssigned(), parent)
        childArr.append(child)

    lenInput = 1
    for x in range(n-1):
        lenInput *= n

    for i in range(lenInput):
        temp = childArr[i]

        for x in range(n):
            if(not temp.getAssignedValue(x)):
                child = Node(n, temp.getWorker(
                ) + 1, x, costMatrix[temp.getWorker() + 1][x], temp.getAssigned(), temp)
                childArr.append(child)

    tempMinChild = Node(n, -1, -1, 2147483647, assignedArr, None)
    for x in range(len(childArr)):
        if(childArr[x].getAssigned() == [True, True, True, True]):
            if(tempMinChild.getCost() > childArr[x].getCost()):
                tempMinChild = childArr[x]

    while(tempMinChild != None):
        tempMinChild.PrintOut()
        tempMinChild = tempMinChild.getParent()


Main()
