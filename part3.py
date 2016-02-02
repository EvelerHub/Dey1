def gcd(a, b):
    modulo = a % b

    if modulo == 0:
        return b
    else:
        return gcd(b, modulo)


inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputMass = inputFile.read().split(" ")

a = abs(int(inputMass[0]))
b = abs(int(inputMass[1]))

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(gcd(min(a, b), max(a, b))))
