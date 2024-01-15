class Queue:
    def __init__(self):
        self.mData = []

    def enqueue(self, item):
        self.mData.append(item)

    def dequeue(self):
        return self.mData.pop(0)

    def front(self):
        return self.mData[0]

q = Queue()
q.enqueue("Hello")
q.enqueue("World")

print(q.front())
q.dequeue()
print(q.front())