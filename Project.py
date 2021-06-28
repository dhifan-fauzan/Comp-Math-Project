import matplotlib.pyplot as plotGraph
import numpy
import sys
import math


def stargihtLineGraph(coefficientOfX, constant, start, end):

    x = numpy.linspace(start, end, 100)
    y = (coefficientOfX * x) + constant

    plotGraph.plot(x, y)
    plotGraph.grid()
    plotGraph.show()

def linearEquation():

    coefficientOfX = int(input("Enter coefficient of x: "))
    constant = int(input("Enter Constant: "))
    startingPoint = int(input("Enter Starting point: "))
    endingPoint = int(input("Enter Ending point: "))

    valuesOfX = []
    valuesOfY = []

    print(f'Your equation is y = {coefficientOfX}x + {constant}\n')

    for i in range(startingPoint, endingPoint + 1):

        y = (coefficientOfX * i) + constant
        print(f'when x = {i}, y = ({coefficientOfX} x {i}) + {constant} = {y}')
        
        valuesOfX.append(i)
        valuesOfY.append(y)
    
    print("\nTable")
    print(f'x : y = {coefficientOfX}x + {constant}')
    for j in range (startingPoint, endingPoint + 1):

        print(f"{valuesOfX[j]} : {valuesOfY[j]}")

    stargihtLineGraph(coefficientOfX, constant, startingPoint, endingPoint)

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

def dotProductOfMatrix():
    
    rows = int(input("Enter Number of Rows for Matrix A: "))
    cols = int(input("Enter Number of Column for Matrix A: "))
    
    print("\nEnter Matrix A Values")
    matrixA = userCreatedMatrix(rows, cols)

    colsB = int(input("\nEnter Number of Column for Matrix B: "))
    print("Enter Matrix B Values")
    matrixB = userCreatedMatrix(cols, colsB)

    print("\nMatrix A")
    print(matrixA)

    print("\nMatrix B")
    print(matrixB)
    print("\nRow R Column C = Sum of multiplication of Row R of Matrix A and Column C of Matrix B")

    for i in range(rows):

        rowOfMatrix = matrixA[i]

        for j in range(colsB):

            answer = 0
            colOfMatrix = matrixB[:, [j]]
            print(f'Row {i+1} Column {j+1} = ', end = "")

            for k in range(cols):

                if k < cols - 1:
                    print(f'{rowOfMatrix[k]} x {colOfMatrix[k][0]}', end = " + ")
                else:
                    print(f'{rowOfMatrix[k]} x {colOfMatrix[k][0]} = ', end = "")

                answer +=  rowOfMatrix[k] * colOfMatrix[k][0]
            
            print(answer)
    
    print(numpy.dot(matrixA, matrixB))
    
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

def gaussEliminationMethod(matrixA = [], newMatrix = True,):

    if newMatrix:
        size = int(input('Enter size of matrix: '))
        matrixA = userCreatedMatrix(size, size)

    else:
        size = len(matrixA)

    print(matrixA)

    for i in range(size):
        if matrixA[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
         
        for j in range(i+1, size):
            print(f'\nRatio = Row {j + 1} Column {i + 1} / Row {i + 1} Column {i + 1}')
            ratio = matrixA[j][i]/matrixA[i][i]
        
            for k in range(size):
                print(f'Row {j + 1} Column {k + 1} = Row {j + 1} Column {k + 1} - Ratio x Row {i + 1} Column {k + 1}')
                print(f'Row {j + 1} Column {k + 1} = {matrixA[j][k]} - {ratio} x {matrixA[i][k]} = ', end ="")
                matrixA[j][k] = matrixA[j][k] - ratio * matrixA[i][k]
                print(matrixA[j][k])
                print(matrixA)

def antiClockWiseRotationOfMatrix():
    
    desiredRotation = int(input("Enter Rotation in Degrees: "))
    theta = math.radians(desiredRotation)

    rotationMatrix = numpy.array([["cos(theta)", "-sin(theta)"],
                                  ["sin(theta)", "cos(theta)" ]])
  
    matrixA = numpy.array([[math.cos(theta), -math.sin(theta)],
                           [math.sin(theta), math.cos(theta) ]])

    cols = int(input("Enter size of column of your Matrix: "))

    print("Enter Matrix Values")
    matrixB = userCreatedMatrix(2, cols)

    print("\nAnti Clockwise Rotation Matrix")
    print(rotationMatrix)

    print("\nYour Matrix")
    print(matrixB)

    print("\nDot Product of Rotation Matrix and User Matrix")
    for i in range(2):

        rowOfMatrix = matrixA[i]

        for j in range(cols):

            answer = 0
            colOfMatrix = matrixB[:, [j]]
            print(f'Row {i+1} Column {j+1} = ', end = "")

            for k in range(2):

                if k < 2 - 1:
                    print(f'{rowOfMatrix[k]} x {colOfMatrix[k][0]}', end = " + ")
                else:
                    print(f'{rowOfMatrix[k]} x {colOfMatrix[k][0]} = ', end = "")

                answer +=  rowOfMatrix[k] * colOfMatrix[k][0]
            
            print(answer)
    
    print("\nRotated Matrix:")
    print(numpy.dot(matrixA, matrixB))

def clockWiseRotationOfMatrix():
    
    desiredRotation = int(input("Enter Rotation in Degrees: "))
    theta = math.radians(desiredRotation)
  
    rotationMatrix = numpy.array([["cos(theta)", "sin(theta)"],
                                  ["-sin(theta)", "cos(theta)" ]])

    matrixA = numpy.array([[math.cos(theta), math.sin(theta)],
                           [-math.sin(theta), math.cos(theta) ]])

    

    cols = int(input("Enter size of column of your Matrix: "))

    print("Enter Matrix Values")
    matrixB = userCreatedMatrix(2, cols)

    print("\nClockwise Rotation Matrix")
    print(rotationMatrix)

    print("\nYour Matrix")
    print(matrixB)
    print("")

    print("\nDot Product of Rotation Matrix and User Matrix")

    for i in range(2):

        rowOfMatrix = matrixA[i]

        for j in range(cols):

            answer = 0
            colOfMatrix = matrixB[:, [j]]
            print(f'Row {i+1} Column {j+1} = ', end = "")

            for k in range(2):

                if k < 2 - 1:
                    print(f'{rowOfMatrix[k]} x {colOfMatrix[k][0]}', end = " + ")
                else:
                    print(f'{rowOfMatrix[k]} x {colOfMatrix[k][0]} = ', end = "")

                answer +=  rowOfMatrix[k] * colOfMatrix[k][0]
            
            print(answer)
    
    print("\nRotated Matrix:")
    print(numpy.dot(matrixA, matrixB))

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
    

def quadraticEquationSolver(a, b, c):
    
    solution1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    solution2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

    print(solution1, 'and', solution2)

def eigenValueOf2x2Matrix():
    
    size = 2
    matrixA = userCreatedMatrix(size, size)

    print("a = 1")
    a = 1

    print(f"\nb = Row 0 Column 0 + Row 1 Column 1")
    print(f'b = {matrixA[0][0]} + {matrixA[1][1]}')
    b = -(matrixA[0][0] + matrixA[1][1])
    print(f"b = {b}")

    print(f"\nc = (Row 0 Column 0 * Row 1 Column 1) - (Row 1 Column 2 * Row 2 Column 1)")
    print(f'c = ({matrixA[0][0]} x {matrixA[1][1]}) - ({matrixA[0][1]} x {matrixA[1][0]})')
    print(f'c = ({matrixA[0][0] * matrixA[1][1]}) - ({matrixA[0][1] * matrixA[1][0]})')
    c = (matrixA[0][0] * matrixA[1][1]) - (matrixA[0][1] * matrixA[1][0])
    print(f'c = {c}')

    print(f"\n{a}x^2 - {-b}x + {c}")
    print("The Eigen Values are: ")
    quadraticEquationSolver(a, b, c)

choice = 0

while choice != 9:

    print("\n Matrix Operations")
    print("1. Basic Operation")
    print("2. Linear Equation")
    print("3. Dot Product")
    print("4. Determinant")
    print("5. Gauss Elimination")
    print("6. Rotation")
    print("7. Transpose")
    print("8. Eigen Values of 2 x 2")
    print("9. Exit")
    choice = int(input("Your Choice: "))

    if choice == 1:

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")

            option = int(input("Your Choice: "))

            if option == 1:
                additionOfMatrix()

            if option == 2:
                subtractionOfMatrix()

            if option == 3:
                multiplicationOfMatrix()


    if choice == 2:
        linearEquation()

    if choice == 3:
        dotProductOfMatrix()

    if choice == 4:

        print("\n1. Determinant 2 x 2")
        print("2. Determinant 3 x 3")

        option = int(input("Your Choice: "))

        if option == 1:
            determinantOf2X2Matrix()

        if option == 2:
            determinantOf3x3Matrix()

    if choice == 5:
        gaussEliminationMethod()

    if choice == 6:

        print("\n1. Clock Wise Rotatiton")
        print("2. Anti Clock Wise Rotation")

        option = int(input("Your Choice: "))

        if option == 1:
            clockWiseRotationOfMatrix()

        if option == 2:
            antiClockWiseRotationOfMatrix()

    if choice == 7:
        transposeOfMatrix()

    if choice == 8:
        eigenValueOf2x2Matrix()