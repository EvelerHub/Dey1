def getKey(item):
    return item[1]


inputFileName = "input.txt"
outputFileName = "output.txt"
with open(inputFileName, "r") as inputFile:
    inputData = inputFile.readlines()

n = int(inputData[0])

times = []
for i in xrange(1, n + 1):
    line = inputData[i].split(" ")

    time = int(line[0]) * 3600 + int(line[1]) * 60 + int(line[2])
    times.append([i, time])

times = sorted(times, key=getKey)

with open(outputFileName, "w") as outputFile:
    for time in times:
        if time[0] != inputData.__len__() - 1:
            outputFile.write(inputData[time[0]])
        else:
            outputFile.write(inputData[time[0]] + "\n")
