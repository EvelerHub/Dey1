import math

vowels = set("aeiouy")


def isVowelContract(currentWord):
    for i in xrange(len(currentWord) - 1):
        if currentWord[i] in vowels and currentWord[i + 1] in vowels:
            return True

    return False


def isEquals(currentWord, word):
    for i in xrange(len(word)):
        if word[i] != currentWord[i]:
            return False

    return True


inputFileName = "anagrams.in"
outputFileName = "anagrams.out"

with open(inputFileName, "r") as inputFile:
    word = inputFile.read()

currentWord = []
for char in word:
    currentWord.append(char)

length = len(word)
masOfAnagrams = []

for k in xrange(math.factorial(length) // length):
    for i in xrange(length):
        currentWord[i], currentWord[(i + 1) % length] = currentWord[(i + 1) % length], currentWord[i]
        breakFlag = isEquals(currentWord, word)
        if isVowelContract(currentWord):
            continue
        if not masOfAnagrams.__contains__(''.join(currentWord)):
            masOfAnagrams.append(''.join(currentWord))

masOfAnagrams.sort()
with open(outputFileName, "w") as outputFile:
    length = len(masOfAnagrams)
    for i in xrange(length):
        outputFile.write(masOfAnagrams[i])
        if i != length - 1:
            outputFile.write("\n")
