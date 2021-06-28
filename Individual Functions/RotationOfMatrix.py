import numpy
import math

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
    
    print("\nOriginal Matrix")
    print(matrixB)
    
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
    
    print("\nOriginal Matrix")
    print(matrixB)

    print("\nRotated Matrix:")
    print(numpy.dot(matrixA, matrixB))

choice = 0

while choice != 3:
    print("1. ClockWise Rotation")
    print("2. Anti Clock Wise Rotation")
    print("3. Exit")
    choice = int(input("Your Choice: "))

    if choice == 1:
        clockWiseRotationOfMatrix()

    if choice == 2:
        antiClockWiseRotationOfMatrix()