class Stack:

    def __init__(self):
        self.stack = list()

    def Push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def Pop(self):
        if len(self.stack) <= 0:
            return ("Stack is empty")
        else:
            return self.stack.pop()

    def Size(self):
        return len(self.stack)
