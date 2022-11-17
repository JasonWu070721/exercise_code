
class Stack:

    def __init__(self):
        self.data = []
        self.index = 0

    # 先進先出
    # Exp:
    # [1, 2]
    def pop(self):
        if self.index <= 0:
            return -1

        self.index -= 1
        return self.data[self.index]

    def push(self, value):

        self.data.append(value)
        self.index += 1


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    data = stack.pop()
    print(data)
    data = stack.pop()
    print(data)
    data = stack.pop()
    print(data)
