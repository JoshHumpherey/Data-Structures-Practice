class Stack:

    def __init__(self):
        self.stack = list()

    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return ("Stack is empty")
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)
