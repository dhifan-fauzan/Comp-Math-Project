import matplotlib.pyplot as plotGraph
import numpy

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

linearEquation()