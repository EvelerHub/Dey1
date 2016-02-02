inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputMass = inputFile.readlines()

rows = int(inputMass[0].split(" ")[0])
columns = int(inputMass[0].split(" ")[1])

matrix = []

minRowIndex = 0
maxRowIndex = 0
minElement = 1001
maxElement = -1001
for i in xrange(rows):
    row = []
    for j in xrange(columns):
        currentElement = int(inputMass[i + 1].split(" ")[j])
        row.append(currentElement)
        if currentElement < minElement:
            minRowIndex = i
            minElement = currentElement
        if currentElement >= maxElement:
            maxRowIndex = i
            maxElement = currentElement
    matrix.append(row)

matrix[maxRowIndex], matrix[minRowIndex] = matrix[minRowIndex], matrix[maxRowIndex]

with open(outputFileName, "w") as outputFile:
    for i in xrange(rows):
        outputFile.write(str(matrix[i]).replace("[", "").replace("]", "").replace(",", "") + "\n")
