def FindMinRow(array, notAllowedIndex):
    min = array[0]
    for x in range(len(array)):
        if(min > array[x] and x != notAllowedIndex):
            min = array[x]
    return min


def FindMinCost(matrix, n):
    count = 0
    for x in range(n):
        count += FindMinRow(matrix[x], x)

    arrayNotAllowedIndex = [None] * n

    for x in range(n):
        count = 0
        tempMin = 100
        for i in range(n):
            count = 0
            count += matrix[x][i]
            for j in range(x + 1, n, 1):
                count += FindMinRow(matrix[j], i)
            if(count < tempMin):
                tempMin = count
        print(tempMin)


def Main():
    n = 4
    costMatrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]

    FindMinCost(costMatrix, n)


Main()
