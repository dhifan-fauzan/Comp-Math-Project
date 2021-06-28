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

def determinantOf2X2Matrix(matrixA = [], newMatrix = True, retrieve = False):

    if newMatrix:
        print("Enter Matrix Values")
        matrixA = userCreatedMatrix(2, 2)

    print("Your Matrix:")
    print(matrixA)

    print("Determinant of a 2 x 2 Matrix is (Row 1 Column 1 x Row 2 Column 2) - (Row 1 Column 2 x Row 2 Column 1)")
    print(f'({matrixA[0][0]} x {matrixA[1][1]}) - ({matrixA[0][1]} x {matrixA[1][0]})')
    print(f'{matrixA[0][0] * matrixA[1][1]} - {matrixA[0][1] * matrixA[1][0]}')

    print("Determinant of Matrix:", matrixA[0][0] * matrixA[1][1] - matrixA[0][1] * matrixA[1][0])

    if retrieve:
        return matrixA[0][0] * matrixA[1][1] - matrixA[0][1] * matrixA[1][0]

def determinantOf3x3Matrix(matrixA = [], newMatrix = True, retrieve = False):

    if newMatrix:
        print("Enter Matrix Values")
        matrixA = userCreatedMatrix(3, 3)

    topRow = matrixA[0]

    remainingRows = matrixA[1:3]

    matrixRight = remainingRows[:, [1, 2]]
    matrixMiddle = remainingRows[:, [0, 2]]
    matrixLeft = remainingRows[:, [0, 1]]

    print("Your 3 x 3 Matrix:")
    print(matrixA)

    print('\nSeperate into 3 Matrices: Right Middle Left')
    print('Right Matrix')
    print(matrixRight)

    print('\nMiddle Matrix')
    print(matrixMiddle)

    print('\nLeft Matrix')
    print(matrixLeft)

    print('\nDeterminant of Right Matrix')
    determinantRight = determinantOf2X2Matrix(matrixRight, newMatrix = False, retrieve = True)

    print('\nDeterminant of Middle Matrix')
    determinantMiddle = determinantOf2X2Matrix(matrixMiddle, newMatrix = False, retrieve = True)

    print('\nDeterminant of Left Matrix')
    determinantLeft = determinantOf2X2Matrix(matrixLeft, newMatrix = False, retrieve = True)

    print("\nDeterminant = Row 1 Column 1 * determinant of Right matrix - Row 1 Column 2 * determinant of Middle matrix + Row 1 Column 3 * determinant of Left matrix")
    print(f"Determinant = {topRow[0]} x {determinantRight} - {topRow[1]} x {determinantMiddle} + {topRow[2]} x {determinantLeft}")
    print(f"Determinant = {topRow[0]*determinantRight} - {topRow[1]*determinantMiddle} + {topRow[2]*determinantLeft}")
    print(f"Determinant = {(topRow[0]*determinantRight) - (topRow[1]*determinantMiddle) + (topRow[2]*determinantLeft)}")

    if retrieve:
        return (topRow[0]*determinantRight) - (topRow[1]*determinantMiddle) + (topRow[2]*determinantLeft)

choice = 0

while choice != 3:

    print("1. Determinant of 2 x 2")
    print("2. Determinant of 3 x 3")
    print("3. Exit")
    choice = int(input("Your Choice: "))

    if choice == 1:
        determinantOf2X2Matrix()

    if choice == 2:
        determinantOf3x3Matrix()