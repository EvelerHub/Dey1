class MyQueue:
    size = 0
    mass = []

    def __init__(self):
        self.size = 0

    def push(self, n):
        self.mass.append(n)
        self.size += 1
        return "ok"

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.mass.pop(0)

        return "error"

    def front(self):
        if self.size > 0:
            return self.mass[0]

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

myQueue = MyQueue()

messages = []
for commandLine in inputCommands:
    command = commandLine.split(" ")
    message = ""
    if command[0] == "push":
        message = str(myQueue.push(int(command[1])))

    if command[0] == "pop\n":
        message = str(myQueue.pop())

    if command[0] == "size\n":
        message = str(myQueue.getSize())

    if command[0] == "front\n":
        message = str(myQueue.front())

    if command[0] == "clear\n":
        message = str(myQueue.clear())

    if command[0] == "exit\n":
        message = "bye"

    messages.append(message)

printMessage(messages)
