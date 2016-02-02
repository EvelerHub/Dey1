inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputMass = inputFile.readlines()

rows = int(inputMass[0].split(" ")[0])
columns = int(inputMass[0].split(" ")[1])

maxElementsInColumns = []
for i in xrange(columns):
    column = []
    for j in xrange(rows):
        column.append(int(inputMass[j + 1].split(" ")[i]))
    maxElementsInColumns.append(max(column))

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(maxElementsInColumns).replace("[", "").replace("]", "").replace(",", ""))
