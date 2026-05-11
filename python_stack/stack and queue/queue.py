class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)
