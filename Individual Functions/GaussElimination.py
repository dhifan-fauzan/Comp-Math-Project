import numpy
import sys

def userCreatedMatrix(rows, cols):

    matrixList = []

    for i in range(0, rows):

        appendingArray = []

        for j in range(0, cols):

            value = int(input(f'Enter row {i + 1} column {j + 1}:'))
            appendingArray.append(value)

        matrixList.append(appendingArray)

    userMatrix = numpy.array(matrixList)

    return userMatrix

def gaussEliminationMethod(matrixA = [], newMatrix = True,):

    if newMatrix:
        size = int(input('Enter size of matrix: '))
        matrixA = userCreatedMatrix(size, size)

    else:
        size = len(matrixA)

    print(matrixA)

    for i in range(size):
        if matrixA[i][i] == 0.0:
            break
         
        for j in range(i+1, size):
            print(f'\nRatio = Row {j + 1} Column {i + 1} / Row {i + 1} Column {i + 1} = ', end="")
            ratio = matrixA[j][i]/matrixA[i][i]
            print(f"{ratio}")
        
            for k in range(size):
                print(f'Row {j + 1} Column {k + 1} = Row {j + 1} Column {k + 1} - Ratio x Row {i + 1} Column {k + 1}')
                print(f'Row {j + 1} Column {k + 1} = {matrixA[j][k]} - {ratio} x {matrixA[i][k]} = ', end ="")
                matrixA[j][k] = matrixA[j][k] - ratio * matrixA[i][k]
                print(matrixA[j][k])
                print(matrixA)

def rankOfMatrix():

    size = int(input("Enter Size of matrix: "))
    matrixA = userCreatedMatrix(size, size)

    gaussEliminationMethod(matrixA, newMatrix = False)

    print("\nrank = total rows - rows with all 0's")
    print(numpy.linalg.matrix_rank(matrixA))

choice = 0

while choice != 3:

    print("1. Gauss Elimination Method")
    print("2. Rank of Array")
    print("3. Exit")
    choice = int(input("Your Choice: "))

    if choice == 1:
        gaussEliminationMethod()

    if choice == 2:
        rankOfMatrix()