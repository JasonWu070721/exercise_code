class Queue:
    def __init__(self):
        self.data = []
        self.index = 0

    def pop(self):
        if self.index <= 0:
            return -1

    def push(self, value):

        self.data.append(value)
        self.index += 1
