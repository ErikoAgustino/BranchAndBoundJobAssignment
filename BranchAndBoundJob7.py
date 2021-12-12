def ReduksiMatrix(n, matrix):
    r = 0
    for x in range(n):
        tempMin = matrix[x][0]
        for i in range(1, n, 1):
            if(tempMin > matrix[x][i]):
                tempMin = matrix[x][i]
        if(tempMin > 0):
            for i in range(n):
                matrix[x][i] -= tempMin
        r += tempMin

    for x in range(n):
        tempMin = matrix[0][x]
        for i in range(1, n, 1):

            if(tempMin > matrix[i][x]):
                tempMin = matrix[i][x]
        if(tempMin > 0):
            for i in range(n):
                matrix[i][x] -= tempMin
        r += tempMin

    return matrix


def main():
    #costMatrix = [[9, 2,  7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
    #costMatrix = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]
    # costMatrix = [[1, 2, 3, 4,5], [2, 1, 3, 4,5], [3, 2, 1, 4,5], [4, 3, 2, 1,5], [4, 3, 2, 5,1]]
    costMatrix = [[10, 12, 19, 11], [5, 10, 7, 8],
                  [12, 14, 13, 11], [8, 15, 11, 9]]
    n = 4
    matrix = ReduksiMatrix(n, costMatrix)
    print(matrix)
    # column
    for x in range(n):
        counter = 0
        index = -1
        for i in range(n):
            print(matrix[x][i])
            if(matrix[x][i] == 0):
                counter += 1
                index = i
        if(counter == 1):
            for j in range(n):
                if(x != j):
                    matrix[j][index] += 1

    # row
    for x in range(n):
        counter = 0
        index = -1
        for i in range(n):
            if(matrix[i][x] < 1):
                counter += 1
                index = i
        if(counter == 1):
            for j in range(n):
                if(x != j):
                    matrix[j][index] += 1

    #costMatrix = [[9, 2,  7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
    costMatrix = [[10, 12, 19, 11], [5, 10, 7, 8],
                  [12, 14, 13, 11], [8, 15, 11, 9]]
    #costMatrix = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]

    for x in range(n):
        for i in range(n):
            if(matrix[x][i] == 0):
                print(costMatrix[x][i])
    print(matrix)


main()
