class MyStack:
    size = 0
    mass = []

    def __init__(self):
        self.size = 0

    def push(self, n):
        self.mass.insert(0, n)
        self.size += 1
        return "ok"

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.mass.pop(0)

        return "error"

    def back(self):
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

myStack = MyStack()

messages = []
for commandLine in inputCommands:
    command = commandLine.split(" ")
    message = ""
    if command[0] == "push":
        message = str(myStack.push(int(command[1])))

    if command[0] == "pop\n":
        message = str(myStack.pop())

    if command[0] == "size\n":
        message = str(myStack.getSize())

    if command[0] == "back\n":
        message = str(myStack.back())

    if command[0] == "clear\n":
        message = str(myStack.clear())

    if command[0] == "exit\n":
        message = "bye"

    messages.append(message)

printMessage(messages)
