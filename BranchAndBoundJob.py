

class Node(object):

    def __init__(self):
        self.parent = None
        self.pathCost = 0
        self.cost = 0
        self.workerID = 0
        self.jobID = 0
        self.assigned = [False for _ in range(DefineConstants.N)]


class comp(object):
    def functorMethod(self, lhs, rhs):
        return lhs.cost > rhs.cost


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    def top(self):
        return self.queue[0]

    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


def newNode(x, y, assigned, parent):
    node = Node()

    for j in range(0, DefineConstants.N):
        node.assigned[j] = assigned[j]
    node.assigned[y] = True

    node.parent = parent
    node.workerID = x
    node.jobID = y

    return node


def calculateCost(costMatrix, x, y, assigned):
    cost = 0

    # to store unavailable jobs
    available = [True]

    # start from next worker
    for i in range(x + 1, DefineConstants.N):
        min = numeric_limits[int].max()
        minIndex = -1

        # do for each job
        for j in range(0, DefineConstants.N):
            # if job is unassigned
            if (not assigned[j]) and available[j] and costMatrix[i][j] < min:
                # store job number
                minIndex = j

                # store cost
                min = costMatrix[i][j]

        # add cost of next worker
        cost += min
        available[minIndex] = False

    return cost


def printAssignments(min):
    if min.parent is None:
        return

    printAssignments(min.parent)
    print("Assign Worker ", end='')
    print(chr((min.workerID + 'A')), end='')
    print(" to Job ", end='')
    print(min.jobID, end='')
    print("\n", end='')


def findMinCost(costMatrix):
    pq = PriorityQueue()

    assigned = [False for _ in range(DefineConstants.N)]
    root = newNode(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.workerID = -1

    pq.push(root)

    while not pq.isEmpty():

        min = pq.top()

        pq.pop()

        i = min.workerID + 1

        if i == DefineConstants.N:
            printAssignments(min)
            return min.cost

        for j in range(0, DefineConstants.N):
            if not min.assigned[j]:
                child = newNode(i, j, min.assigned, min)

                child.pathCost = min.pathCost + costMatrix[i][j]

                child.cost = child.pathCost + \
                    calculateCost(costMatrix, i, j, child.assigned)

                pq.push(child)


def main():
    costMatrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]

    print("\nOptimal Cost is ", end='')
    print(findMinCost(costMatrix), end='')


class DefineConstants(object):
    N = 4


main()
