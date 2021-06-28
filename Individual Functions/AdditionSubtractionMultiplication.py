import numpy

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

def additionOfMatrix():

    rows = int(input("Enter Number of Rows: "))
    cols = int(input("Enter Number of Column: "))

    print("\nEnter Matrix A Values")
    matrixA = userCreatedMatrix(rows, cols)

    print("\nEnter Matrix B Values")
    matrixB = userCreatedMatrix(rows, cols)

    print("\nMatrix A")
    print(matrixA)

    print("\nMatrix B")
    print(matrixB)
    print("\nRow R Column C = Row R Column C of Matrix A + Row R Column C of Matrix B")

    for i in range(0, rows):

        for j in range(0, cols):

            print(f'Row {i+1} Column {j+1} = {matrixA[i][j]} + {matrixB[i][j]} = {matrixA[i][j] + matrixB[i][j]}')

    print("\nAddition of Matrix A and B")
    print(matrixA + matrixB)

def subtractionOfMatrix():

    rows = int(input("Enter Number of Rows: "))
    cols = int(input("Enter Number of Column: "))

    print("\nEnter Matrix A Values")
    matrixA = userCreatedMatrix(rows, cols)

    print("\nEnter Matrix B Values")
    matrixB = userCreatedMatrix(rows, cols)

    print("\nMatrix A")
    print(matrixA)

    print("\nMatrix B")
    print(matrixB)
    print("\nRow R Column C = Row R Column C of Matrix A - Row R Column C of Matrix B")

    for i in range(0, rows):

        for j in range(0, cols):

            print(f'Row {i+1} Column {j+1} = {matrixA[i][j]} - {matrixB[i][j]} = {matrixA[i][j] - matrixB[i][j]}')

    print("\nSubtraction of Matrix A and B")
    print(matrixA - matrixB)

def multiplicationOfMatrix():

    rows = int(input("Enter Number of Rows: "))
    cols = int(input("Enter Number of Column: "))

    print("\nEnter Matrix A Values")
    matrixA = userCreatedMatrix(rows, cols)

    print("\nEnter Matrix B Values")
    matrixB = userCreatedMatrix(rows, cols)

    print("\nMatrix A")
    print(matrixA)

    print("\nMatrix B")
    print(matrixB)
    print("\nRow R Column C = Row R Column C of Matrix A x Row R Column C of Matrix B")

    for i in range(0, rows):

        for j in range(0, cols):

            print(f'Row {i+1} Column {j+1} = {matrixA[i][j]} x {matrixB[i][j]} = {matrixA[i][j] * matrixB[i][j]}')

    print("\nMultiplication of Matrix A and B")
    print(matrixA * matrixB)

choice = 0

while choice != 4:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")
    choice = int(input("Your Choice: "))

    if choice == 1:
        additionOfMatrix()

    if choice == 2:
        subtractionOfMatrix()

    if choice == 3:
        multiplicationOfMatrix()