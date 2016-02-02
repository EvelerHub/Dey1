inputFileName = "input.txt"


def getCuttingNumber(number, maxCaunt):
    if maxCount < number:
        return maxCount
    else:
        return number


outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    maxCount = int(inputFile.readline())
    snowflakes = inputFile.readline().split(" ")

whiteSnowflake = getCuttingNumber(int(snowflakes[0]), maxCount)
blueSnowflake = getCuttingNumber(int(snowflakes[1]), maxCount)
pinkSnowflake = getCuttingNumber(int(snowflakes[2]), maxCount)
arrayOfSnowflakes = [whiteSnowflake, blueSnowflake, pinkSnowflake]
arrayOfSnowflakes.sort()
sumOfOfSnowflakes = sum(arrayOfSnowflakes)

count = 0
if sumOfOfSnowflakes >= maxCount:
    i = 0

    while i <= arrayOfSnowflakes[0]:
        j = 0
        while j <= arrayOfSnowflakes[1]:
            k = 0
            while k <= arrayOfSnowflakes[2]:
                if (i + j + k) == maxCount:
                    count += 1
                k += 1
            j += 1
        i += 1

with open(outputFileName, "w") as outputFile:
    outputFile.write(str(count))
