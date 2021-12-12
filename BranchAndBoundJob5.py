class Node:
    def __init__(self, n, worker, job, cost, assigned, parent):
        self.parent = parent
        self.worker = worker
        self.job = job
        self.cost = cost
        self.totalCost = 0

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

    def getTotalCost(self):
        return self.totalCost

    def setTotalCost(self, totalCost):
        self.totalCost = totalCost

    def PrintOut(self):
        print("Parent:", self.getParent())
        print("Worker:", self.getWorker())
        print("Job:", self.getJob())
        print("Cost:", self.getCost())
        print("Total Cost:", self.getTotalCost())
        print("Assigned:", self.getAssigned())
        print()


def FindMinRow(worker, parent, matrix, assigned):
    result = []
    while(parent != None):
        result.append(parent.getCost())
        parent = parent.getParent()

    for x in range(worker+1, len(matrix), 1):
        tempIndex = 0
        while(assigned[tempIndex]):
            tempIndex += 1

        tempMin = matrix[x][tempIndex]
        for i in range(1, len(matrix), 1):
            if(tempMin > matrix[x][i] and not assigned[i]):
                tempMin = matrix[x][i]

        result.append(tempMin)
    return result


def SumArr(arr):
    result = 0
    for x in arr:
        result += x
    return result


def Elimination(array):
    tempMin = Node(4, -1, -1, 0, [False, False, False, False], None)
    tempMin.setTotalCost(2147483647)
    for x in array:
        if(tempMin.getTotalCost() > x.getTotalCost()):
            tempMin = x

    result = FindDuplicate(array, tempMin)
    return result


def FindDuplicate(array, minValue):
    result = []
    for x in array:
        if(x.getTotalCost() == minValue.getTotalCost()):
            result.append(x)
    return result


def Main():
    n = 4
    #costMatrix = [[9, 2,  7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
    costMatrix = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]
    #costMatrix = [[1, 2, 3, 4,5], [2, 1, 3, 4,5], [3, 2, 1, 4,5], [4, 3, 2, 1,5], [4, 3, 2, 5,1]]
    #costMatrix = [[10, 12, 19, 11], [5, 10, 7, 8],[12, 14, 13, 11], [8, 15, 11, 9]]
    assignedArr = [False] * n

    array = []

    # root
    root = Node(n, -1, -1, 0, assignedArr, None)
    array.append(root)

    foundLeaf = []

    while(len(array) > 0):
        temp = array.pop(0)

        for x in range(n):
            if(not temp.getAssignedValue(x)):
                child = Node(n, temp.getWorker(
                ) + 1, x, costMatrix[temp.getWorker() + 1][x], temp.getAssigned(), temp)
                costMin = FindMinRow(child.getWorker(), child,
                                     costMatrix, child.getAssigned())
                child.setTotalCost(SumArr(costMin))
                array.append(child)

                if(not False in child.getAssigned()):
                    foundLeaf.append(child)
        array = Elimination(array)

    # for x in array:
    #    x.PrintOut()
    # print(len(array))

    b = Elimination(foundLeaf)

    for leaf in b:
        leaf.PrintOut()


Main()
