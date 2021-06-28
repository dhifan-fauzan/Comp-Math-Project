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

eigenValueOf2x2Matrix()