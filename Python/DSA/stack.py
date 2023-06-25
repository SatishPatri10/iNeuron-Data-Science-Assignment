Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def isEmpty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.isEmpty())
print(stack.pop())
print(stack.isEmpty())
