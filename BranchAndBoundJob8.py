class Node:
    def __init__(self, n, job, worker, assigned, parent, paramMatrix):
        self.parent = parent
        self.job = job
        self.worker = worker
        self.r = 0

        self.matrix = [None] * n
        for x in range(n):
            self.matrix[x] = paramMatrix[x].copy()

        self.n = n

        self.assigned = assigned.copy()

        if(self.parent != None):
            self.r += self.parent.r

        if(job > -1):
            self.setAssignedValue(True, job)
            self.r += self.matrix[worker][job]

        self.ReduksiMatrix()

    def ReduksiMatrix(self):
        for x in range(self.job + 1, self.n, 1):
            index = 0
            while(self.getAssignedValue(index) and index+1 < self.n):
                index += 1
            tempMin = self.matrix[x][index]

            for i in range(self.n):
                if(tempMin > self.matrix[x][i] and not self.getAssignedValue(i)):

                    tempMin = self.matrix[x][i]

            if(tempMin > 0):
                for i in range(self.n):
                    if(not self.getAssignedValue(i) or self.matrix[x][i] > 0):
                        self.matrix[x][i] -= tempMin
            self.r += tempMin

        for x in range(self.worker + 1, self.n, 1):
            index = 0
            while(self.getAssignedValue(index) and index+1 < self.n):
                index += 1
            tempMin = self.matrix[index][x]
            for i in range(self.n):
                if(tempMin > self.matrix[i][x] and not self.getAssignedValue(i)):
                    tempMin = self.matrix[i][x]
            if(tempMin > 0):
                for i in range(self.n):
                    if(not self.getAssignedValue(i) or self.matrix[x][i] > 0):
                        self.matrix[i][x] -= tempMin
            self.r += tempMin

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
        print("R:", self.r)
        print("Assigned:", self.getAssigned())
        print("matrix:", self.matrix)
        print()


def Elimination(array):
    if(len(array) > 0):
        tempMin = array[0]

        for x in array:
            if(tempMin.r > x.r):
                tempMin = x

        result = FindDuplicate(array, tempMin)
        return result
    return []


def FindDuplicate(array, minValue):
    result = []
    for x in array:
        if(x.r == minValue.r):
            result.append(x)
    return result


def main():
    #costMatrix = [[9, 2,  7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
    #costMatrix = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]
    #costMatrix = [[1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [3, 2, 1, 4, 5], [4, 3, 2, 1, 5], [4, 3, 2, 5, 1]]
    costMatrix = [[10, 12, 19, 11], [5, 10, 7, 8],
                  [12, 14, 13, 11], [8, 15, 11, 9]]
    #costMatrix = [[1,60,46,37,16,32,50,19,44,39], [31,27,48,25,34,54,43,21,6,54], [44,24,73,24,96,53,43,52,12,78], [4,90,100,21,60,80,72,40,93,23], [29,37,58,29,50,25,98,95,74,23], [33,84,66,100,34,99,61,6,31,19], [28,58,5,60,18,79,15,50,24,39], [26,2,32,60,79,59,32,45,78,3],[27,11,8,22,70,6,92,88,61,82], [59,77,94,64,66,22,56,84,38,36]]

    n = 4
    arrAssigned = [False] * n
    root = Node(n, -1, -1, arrAssigned, None, costMatrix)

    root.PrintOut()

    array = []
    array.append(root)

    """
    tempMatrix = temp.matrix.copy()

    child = Node(n,  0, temp.getWorker() + 1,
                 temp.getAssigned(), temp, tempMatrix)
    child.PrintOut()

    child2 = Node(n,  1, temp.getWorker() + 1,
                  temp.getAssigned(), temp, tempMatrix)
    child2.PrintOut()

    temp.PrintOut()
"""
    foundLeaf = []

    while(len(array) > 0):

        print(len(array))
        tempArr = array.copy()

        array = []

        for i in range(len(tempArr)):
            temp = tempArr.pop(0)
            for x in range(n):
                if(not temp.getAssignedValue(x)):
                    child = Node(n, x, temp.getWorker(
                    ) + 1,  temp.getAssigned(), temp, temp.matrix)

                    if(not False in child.getAssigned()):
                        foundLeaf.append(child)
                    else:
                        array.append(child)
            array = Elimination(array.copy())

    # for x in array:
    #    x.PrintOut()
    # print(len(array))

    b = Elimination(foundLeaf)

    # for child in b:
    #    child.PrintOut()

    test = b[0]
    totalCost = 0
    while(test.getParent() != None):
        # test.PrintOut()
        print("Worker: " + str(test.getWorker()))
        print("Job: " + str(test.getJob()))
        print("Cost: " + str(costMatrix[test.getWorker()][test.getJob()]))
        print()
        totalCost += costMatrix[test.getWorker()][test.getJob()]
        test = test.getParent()

    print("Total Cost: " + str(totalCost))


main()
