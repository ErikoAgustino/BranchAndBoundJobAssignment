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
        # Row
        for x in range(self.worker + 1, self.n, 1):
            tempMin = 2147483647

            for i in range(self.n):
                if(tempMin > self.matrix[x][i] and not self.getAssignedValue(i)):
                    tempMin = self.matrix[x][i]

            if(tempMin > 0):
                for i in range(self.n):
                    if(not self.getAssignedValue(i)):
                        if(self.matrix[x][i] > 0):
                            self.matrix[x][i] -= tempMin
            self.r += tempMin

        # Column
        for x in range(self.n):
            tempMin = 0
            if(not self.getAssignedValue(x)):
                tempMin = 2147483647
                for i in range(self.worker + 1, self.n, 1):
                    if(tempMin > self.matrix[i][x]):
                        tempMin = self.matrix[i][x]

            if(tempMin > 0):
                for i in range(self.worker + 1, self.n, 1):
                    if(self.matrix[i][x] > 0):
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
            # print(x.r)
            if(tempMin.r > x.r):
                tempMin = x

        # print("batas")
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
    # 13 Ok
    #costMatrix = [[9, 2,  7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]

    # 4 OK
    # costMatrix = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]

    # 5 OK
    # costMatrix = [[1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [3, 2, 1, 4, 5], [4, 3, 2, 1, 5], [4, 3, 2, 5, 1]]

    # 38 OK
    # costMatrix = [[10, 12, 19, 11], [5, 10, 7, 8],[12, 14, 13, 11], [8, 15, 11, 9]]

    # 126 OK
    # costMatrix = [[1, 60, 46, 37, 16, 32, 50, 19, 44, 39], [31, 27, 48, 25, 34, 54, 43, 21, 6, 54], [44, 24, 73, 24, 96, 53, 43, 52, 12, 78], [4, 90, 100, 21, 60, 80, 72, 40, 93, 23], [29, 37, 58, 29, 50, 25, 98, 95, 74, 23], [
    #    33, 84, 66, 100, 34, 99, 61, 6, 31, 19], [28, 58, 5, 60, 18, 79, 15, 50, 24, 39], [26, 2, 32, 60, 79, 59, 32, 45, 78, 3], [27, 11, 8, 22, 70, 6, 92, 88, 61, 82], [59, 77, 94, 64, 66, 22, 56, 84, 38, 36]]

    # 153
    # costMatrix = [[91, 19, 96, 49, 80, 72, 31, 13, 80, 7, 27, 98, 82, 49, 91], [17, 88, 89, 62, 75, 23, 74, 29, 6, 67, 62, 7, 97, 92, 6], [89, 41, 18, 16, 24, 64, 38, 79, 68, 52, 30, 63, 56, 87, 2], [54, 21, 70, 31, 66, 1, 86, 66, 38, 48, 63, 23, 2, 5, 48], [89, 84, 31, 20, 69, 45, 47, 46, 24, 75, 45, 99, 48, 42, 8], [97, 3, 11, 70, 75, 29, 61, 8, 100, 8, 32, 55, 71, 35, 15], [25, 27, 26, 54, 58, 84, 30, 60, 83, 62, 35, 48, 45, 79, 81], [60, 37, 31, 30, 67, 92,
    #                                                                                                                                                                                                                                                                                                                                                                                                                                                    83, 63, 23, 54, 66, 79, 92, 11, 41], [33, 74, 85, 68, 42, 5, 13, 17, 19, 6, 13, 3, 78, 17, 34], [64, 50, 29, 54, 59, 17, 30, 85, 10, 80, 29, 74, 4, 63, 100], [38, 43, 1, 78, 26, 40, 78, 54, 16, 12, 79, 66, 66, 4, 6], [80, 66, 74, 77, 14, 96, 1, 71, 8, 51, 88, 15, 66, 72, 34], [46, 46, 65, 10, 93, 48, 13, 79, 48, 58, 81, 98, 91, 37, 45], [40, 77, 94, 95, 51, 55, 17, 19, 88, 83, 96, 93, 86, 73, 79], [97, 19, 29, 22, 25, 38, 76, 59, 90, 15, 82, 84, 57, 10, 37]]

    # 123
    costMatrix = [[38, 11, 97, 3, 75, 4, 89, 26, 91, 99], [43, 47, 48, 16, 60, 92, 75, 47, 22, 52], [21, 92, 29, 9, 88, 46, 81, 62, 11, 62], [37, 46, 38, 69, 10, 43, 2, 69, 9, 71], [76, 20, 90, 68, 18, 63, 69, 60, 16, 5], [
        89, 100, 34, 32, 99, 25, 98, 17, 27, 98], [33, 70, 50, 87, 53, 50, 2, 11, 42, 31], [46, 13, 10, 26, 70, 84, 55, 50, 40, 99], [8, 89, 36, 69, 63, 51, 71, 46, 15, 41], [37, 55, 99, 66, 35, 68, 50, 25, 32, 57]]

    # 133 OK
    # costMatrix = [[21, 95, 98, 6, 94, 2, 64, 70], [65, 23, 90, 5, 33, 95, 67, 38], [90, 22, 42, 60, 67, 29, 8, 92], [90, 26, 99, 93, 46, 95, 35, 89], [
    #    98, 32, 42, 34, 83, 62, 48, 32], [89, 63, 6, 70, 92, 75, 11, 5], [16, 19, 35, 63, 70, 67, 91, 40], [70, 66, 63, 10, 73, 68, 56, 36]]

    n = 10
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
        tempArr = array.copy()

        array = []

        for i in range(len(tempArr)):
            temp = tempArr.pop(0)
            temp.PrintOut()
            for x in range(n):
                if(not temp.getAssignedValue(x)):
                    child = Node(n, x, temp.getWorker(
                    ) + 1,  temp.getAssigned(), temp, temp.matrix)
                    # for j in range(n):
                    #   print(child.matrix[j])
                    # print()
                    if(not False in child.getAssigned()):
                        foundLeaf.append(child)
                    else:
                        array.append(child)
            array = Elimination(array.copy())

        print("batas")
        print()

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


def JobAssigment(costMatrix):
    n = len(costMatrix[0])
    arrAssigned = [False] * n
    root = Node(n, -1, -1, arrAssigned, None, costMatrix)

    array = []
    array.append(root)

    foundLeaf = []

    while(len(array) > 0):
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

    b = Elimination(foundLeaf)

    return b


# main()
