class MyDeck:
    size = 0
    mass = []

    def __init__(self):
        self.size = 0

    def push_back(self, n):
        self.mass.append(n)
        self.size += 1
        return "ok"

    def push_front(self, n):
        self.mass.insert(0, n)
        self.size += 1
        return "ok"

    def pop_front(self):
        if self.size > 0:
            self.size -= 1
            return self.mass.pop(0)

        return "error"

    def pop_back(self):
        if self.size > 0:
            self.size -= 1
            return self.mass.pop()

        return "error"

    def front(self):
        if self.size > 0:
            return self.mass[0]

        return "error"

    def back(self):
        if self.size > 0:
            return self.mass[self.size - 1]

        return "error"

    def clear(self):
        self.mass = []
        self.size = 0
        return "ok"

    def getSize(self):
        return self.size


def printMessage(messages):
    messagesWithSeparators = ""
    for message in messages:
        messagesWithSeparators += message + "\n"

    with open(outputFileName, "w") as outputFile:
        outputFile.writelines(messagesWithSeparators)


inputFileName = "input.txt"
outputFileName = "output.txt"

with open(inputFileName, "r") as inputFile:
    inputCommands = inputFile.readlines()

myDeck = MyDeck()

messages = []
for commandLine in inputCommands:
    command = commandLine.split(" ")
    message = ""
    if command[0] == "push_front":
        message = str(myDeck.push_front(int(command[1])))

    if command[0] == "push_back":
        message = str(myDeck.push_back(int(command[1])))

    if command[0] == "pop_front\n":
        message = str(myDeck.pop_front())

    if command[0] == "pop_back\n":
        message = str(myDeck.pop_back())

    if command[0] == "size\n":
        message = str(myDeck.getSize())

    if command[0] == "front\n":
        message = str(myDeck.front())

    if command[0] == "back\n":
        message = str(myDeck.back())

    if command[0] == "clear\n":
        message = str(myDeck.clear())

    if command[0] == "exit\n":
        message = "bye"

    messages.append(message)

    if command[0] == "exit\n":
        break

printMessage(messages)
