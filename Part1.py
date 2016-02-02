inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputMass = inputFile.read().split(" ")

perimeter = 2 * int(inputMass[0]) + 2 * int(inputMass[1])
square = int(inputMass[0]) * int(inputMass[1])

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(perimeter))
    outputFile.write()
    outputFile.write(str(square))
