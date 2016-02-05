inputFileName = "input.txt"
outputFileName = "output.txt"
with open(inputFileName, "r") as inputFile:
    inputData = inputFile.readlines()

line1 = inputData[0].split(" ")
line2 = inputData[1].split(" ")

cards1 = []
cards2 = []

for i in xrange(5):
    card1 = int(line1[i])
    card2 = int(line2[i])
    cards1.append(card1)
    cards2.append(card2)

turnsCount = 0

while turnsCount <= 1000000:
    if cards1.__len__() == 10:
        break

    if cards2.__len__() == 10:
        break

    card1 = cards1.pop(0)
    card2 = cards2.pop(0)

    if card1 == 0 and card2 == 9:
        cards1.append(card1)
        cards1.append(card2)
        turnsCount += 1
        continue

    if card2 == 0 and card1 == 9:
        cards2.append(card1)
        cards2.append(card2)
        turnsCount += 1
        continue

    if card1 > card2:
        cards1.append(card1)
        cards1.append(card2)
    else:
        cards2.append(card1)
        cards2.append(card2)

    turnsCount += 1

with open(outputFileName, "w") as outputFile:
    if turnsCount > 1000000:
        outputFile.write("Botva")

    if cards1.__len__() == 10:
        outputFile.write("Artur " + str(turnsCount))

    if cards2.__len__() == 10:
        outputFile.write("Igor " + str(turnsCount))
