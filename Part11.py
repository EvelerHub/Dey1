inputFileName = "input.txt"
outputFileName = "output.txt"
with open(inputFileName, "r") as inputFile:
    inputData = inputFile.readlines()

vertices = int(inputData[0][0])

adjacencyMatrix = []
for i in xrange(1, vertices + 1):
    lineOfInputData = inputData[i].split(" ")
    line = []
    for j in xrange(vertices):
        line.append(int(lineOfInputData[j]))
    adjacencyMatrix.append(line)

vectorOfStocks = []
vectorOfSources = []

for i in xrange(vertices):
    vectorOfStocks.append(True)
    vectorOfSources.append(True)

for i in xrange(vertices):
    for j in xrange(vertices):
        if adjacencyMatrix[i][j] == 1:
            vectorOfStocks[i] = False
            vectorOfSources[j] = False

indexesOfSources = []
indexesOfStocks = []
countOfSources = 0
countOfStocks = 0

for i in xrange(vertices):
    if vectorOfSources[i]:
        indexesOfSources.append(i + 1)
        countOfSources += 1
    if vectorOfStocks[i]:
        indexesOfStocks.append(i + 1)
        countOfStocks += 1

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(countOfSources))
    if countOfSources > 0:
        outputFile.write(" ")
    for i in xrange(countOfSources):
        outputFile.write(str(indexesOfSources[i]))
        if i < countOfSources - 1:
            outputFile.write(" ")
    outputFile.write("\n")

    outputFile.write(str(countOfStocks))
    if countOfStocks > 0:
        outputFile.write(" ")
    for i in xrange(countOfStocks):
        outputFile.write(str(indexesOfStocks[i]))
        if i < countOfStocks - 1:
            outputFile.write(" ")
