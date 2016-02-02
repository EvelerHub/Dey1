inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    k = int(inputFile.read())

result = 0
if k % 4 == 0:
    result = 4

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(result))
