import math


def getPrimeNumbers(number):
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

    simpleNumbers = []
    for i in xrange(number):
        if mas[i] == 0:
            simpleNumbers.append(i + 1)

    return simpleNumbers


def isContainTwoness(number):
    while number > 0:
        if number % 2 == 0:
            return 1
        number //= 10

    return 0 


inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    number = int(inputFile.read())

mas = getPrimeNumbers(number)

count = 0

for i in mas:
    if isContainTwoness(i) != 1:
        count += 1

if count <= 0:
    count = 0
else:
    count -= 1

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(count))
