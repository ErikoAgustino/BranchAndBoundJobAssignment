class Node:
    def __init__(self, n, worker, job, assigned, parent):
        self.pathCost = 0
        self.cost = 0

        self.parent = parent
        self.worker = worker
        self.job = job

        self.assigned = [False] * n
        for x in range(n):
            self.assigned[x] = assigned[x]

        if(job > -1):
            self.setAssignedValue(True, job)

    def setPathCost(self, pathCost):
        self.pathCost = pathCost

    def setCost(self, cost):
        self.cost = cost

    def setAssignedValue(self, value, index):
        self.assigned[index] = value

    def getAssigned(self):
        return self.assigned

    def getAssignedValue(self, index):
        return self.assigned[index]

    def getJob(self):
        return self.job

    def getWorker(self):
        return self.worker

    def getParent(self):
        return self.parent

    def getPathCost(self):
        return self.pathCost

    def getCost(self):
        return self.cost

    def addChild(self, node):
        self.child.append(node)

    def getChildCount(self):
        return len(self.child)

    def getChildern(self):
        return self.child

    def getIndex(self):
        return self.index


class Queue():
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        try:
            max = 0
            for x in range(len(self.queue)):
                if self.queue[x].getCost() > self.queue[max].getCost():
                    max = x
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


def CalculateCost(matrix, worker, job, assigned, n):
    cost = 0

    available = [False] * n
    available[0] = True

    for x in range(worker + 1, n, 1):
        min = 2000
        minIndex = -1
        for i in range(n):
            if(not assigned[i] and available[i] and matrix[x][i] < min):
                minIndex = i
                min = matrix[x][i]
        cost += min
        available[minIndex] = False
    return cost


def CostComparison(node1, node2):
    return node1.getCost() > node2.getCost()


def PrintResult(node, matrix):
    if(not node.getParent() == None):
        PrintResult(node.getParent(), matrix)
        print("Worker", node.getWorker(), "to Job", node.getJob(),
              "Cost:", matrix[node.getWorker()][node.getJob()])


def FindMinRow(array, notAllowedIndex):
    min = array[0]
    for x in range(len(array)):
        if(min > array[x] and x != notAllowedIndex):
            min = array[x]
    return min

    count = 0
    for x in range(n):
        count += FindMinRow(matrix[x], x)
    root = Node(count, -1)

    for x in range(n):
        count = 0
        tempMin = []
        for i in range(n):
            count = 0
            count += matrix[x][i]
            for j in range(x + 1, n, 1):
                count += FindMinRow(matrix[j], i)
            tempMin.append(count)
        minValue = min(tempMin)
        print(minValue)


def FindMinCost(matrix, n):
    queue = Queue()

    assigned = [False] * n
    root = Node(n, -1, -1, assigned, None)

    queue.push(root)

    while(not queue.isEmpty()):
        temp = queue.pop()
        res = temp.getWorker() + 1
        if(res == n):
            pass
            #PrintResult(temp, matrix)

        for x in range(n):
            print(res)
            print()
            if(not temp.getAssignedValue(x)):

                child = Node(n, res, x, temp.getAssigned(), temp)
                child.setPathCost(temp.getPathCost() + matrix[res][x])
                child.setCost(child.getPathCost() +
                              CalculateCost(matrix, res, x, child.assigned, n))

                queue.push(child)


def Main():
    n = 4
    costMatrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]

    FindMinCost(costMatrix, n)


Main()
