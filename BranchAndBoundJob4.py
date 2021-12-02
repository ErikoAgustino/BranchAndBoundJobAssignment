class Node:
    def __init__(self, n, worker, job, cost, assigned, parent):
        self.parent = parent
        self.worker = worker
        self.job = job
        self.cost = cost

        self.assigned = [False] * n
        for x in range(n):
            self.assigned[x] = assigned[x]

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

    assignedArr = [False] * n

    childArr = []

    # parent
    parent = Node(n, -1, -1, 0, assignedArr, None)
    for x in range(n):
        child = Node(n, parent.getWorker() + 1, x,
                     costMatrix[parent.getWorker() + 1][x], parent.getAssigned(), parent)
        childArr.append(child)

    lenInput = 1
    for x in range(1, n+1, 1):
        lenInput *= x

    for i in range(lenInput):
        temp = childArr[i]

        for x in range(n):
            if(not temp.getAssignedValue(x)):
                child = Node(n, temp.getWorker(
                ) + 1, x, costMatrix[temp.getWorker() + 1][x], temp.getAssigned(), temp)
                childArr.append(child)

    for x in range(len(childArr)):
        childArr[x].PrintOut()


Main()
