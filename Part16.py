import math

inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputFileLines = inputFile.readlines()

points = []
for i in xrange(3):
    coordinates = inputFileLines[i].split(" ")
    points.append([int(coordinates[0]), int(coordinates[1])])

angles = []
for i in xrange(3):
    x1 = points[(i + 1) % 3][0] - points[i][0]
    x2 = points[(i + 2) % 3][0] - points[i][0]

    y1 = points[(i + 1) % 3][1] - points[i][1]
    y2 = points[(i + 2) % 3][1] - points[i][1]

    scalar = x1 * x2 + y1 * y2

    module1 = math.sqrt(x1 ** 2 + y1 ** 2)
    module2 = math.sqrt(x2 ** 2 + y2 ** 2)

    angle = math.acos(scalar / (module1 * module2))

    angles.append(angle * 180 / math.pi)

angles.sort()

with open(outputFileName, "w") as outputFile:
    outputFile.writelines("%.6f" % angles[2])
