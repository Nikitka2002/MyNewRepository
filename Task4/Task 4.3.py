class MyQueue:
    queue = []
    def __init__(self,items = list(input())):
        self.queue = items
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        self.queue.pop()
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        if(len(self.queue)==0):
            return 'queue is empty'
        else:
            return "queue is not empty"


Queue = MyQueue()
Queue.enqueue(7)
Queue.dequeue()
print(Queue.size())
print(Queue.isEmpty())
