def fastExp(a, n, m):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0

    if n == 0:
        return 1
    if even(n):
        return fastExp(a, n / 2, m) ** 2 % m
    return a * fastExp(a, n - 1, m) % m


inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputFileArray = inputFile.readline().split(" ")

a = int(inputFileArray[0])
b = int(inputFileArray[1])
m = int(inputFileArray[2])

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(fastExp(a, b, m)))
