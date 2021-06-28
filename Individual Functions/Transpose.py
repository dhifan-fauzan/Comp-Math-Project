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

def transposeOfMatrix():

    rows = int(input("Enter Number of Rows for Matrix A: "))
    cols = int(input("Enter Number of Column for Matrix A: "))

    matrixA = userCreatedMatrix(rows, cols)
    transposedMatrix = numpy.zeros((cols, rows))

    for i in range(rows):

        for j in range(cols):

            print(f'Transpose Matrix Row {j + 1} Column {i + 1} = Original Matrix Row {i + 1} Column {j + 1}')
            transposedMatrix[j][i] = matrixA[i][j]
            print(transposedMatrix)

    print("\nOriginal Matrix")
    print(matrixA)
    print('\nTransposed Matrix')
    print(transposedMatrix)

transposeOfMatrix()