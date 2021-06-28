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

dotProductOfMatrix()