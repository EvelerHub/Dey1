inputFileName = "dfs.in"
outputFileName = "dfs.out"
with open(inputFileName, "r") as inputFile:
    inputData = inputFile.readlines()

vertices = int(inputData[0].split(" ")[0])
vertex = int(inputData[0].split(" ")[1])

adjacencyMatrix = []
for i in xrange(1, vertices + 1):
    lineOfInputData = inputData[i].split(" ")
    line = []
    for j in xrange(vertices):
        line.append(int(lineOfInputData[j]))
    adjacencyMatrix.append(line)

count = 1

for i in xrange(vertices):
    if adjacencyMatrix[vertex][i] == 1 and adjacencyMatrix[i][vertex] == 1:
        count += 1

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(count))
