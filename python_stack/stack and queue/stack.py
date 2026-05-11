class stack:
 
    def __init__ (self):
        self.list = []
 
    def push(self, item):
        self.list.append(item)
 
    def pop(self):
        return self.list.pop()
 
    def peek(self):
        return self.list[-1]
 
    def print(self):
        print(self.list)
 
 
test = stack()
test.push(1)
test.push(2)
test.push(3)
test.push(4)
test.push(5)
test.push(6)
test.push(7)
print(test.peek())
print(test.pop())
print(test.peek())
print(test.pop())
print(test.peek())
test.print()