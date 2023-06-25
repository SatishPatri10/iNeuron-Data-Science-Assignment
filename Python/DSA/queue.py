Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.isEmpty())
print(queue.dequeue())
print(queue.isEmpty())
