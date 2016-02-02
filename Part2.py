import math


def getPreviousPrimeNumber(number):
    mas = []
    for i in xrange(number):
        mas.append(0)

    i = 1
    while i < math.sqrt(number):
        if mas[i] == 0:
            j = i * 2 + 1
            while j < number:
                mas[j] = 1
                j += i + 1
        i += 1

    for i in xrange(number):
        index = number - i - 1
        if mas[index] == 0:
            return index + 1

    return number


def isPrimeNumber(number):
    for i in xrange(2, number):
        if number % i == 0:
            return 0

        if i == number or i >= math.sqrt(number):
            return 1

    return 1


def getNextPrimeNumber(number):
    i = number

    while isPrimeNumber(i) == 0:
        i += 1

    return i


inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    number = int(inputFile.read())

previousPrimeNumber = getPreviousPrimeNumber(number)

nextPrimeNumber = getNextPrimeNumber(number)

with open(outputFileName, "w") as outputFile:
    if (number - previousPrimeNumber) <= (nextPrimeNumber - number):
        outputFile.write(str(previousPrimeNumber))
    else:
        outputFile.write(str(nextPrimeNumber))
