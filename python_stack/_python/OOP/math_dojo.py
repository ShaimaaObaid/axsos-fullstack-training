class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num

        for n in nums:
            self.result += n

        return self

    def subtract(self, num, *nums):
        self.result -= num

        for n in nums:
            self.result -= n

        return self

# TEST 1
md1 = MathDojo()
print(md1.add(2).result)                  
print(md1.add(2, 5, 1).result)           
print(md1.subtract(3, 2).result)        

# TEST 2
md2 = MathDojo()
print(md2.add(10, 20).result)            
print(md2.subtract(5).result)             
print(md2.subtract(2, 3).result)          

# TEST 3
md3 = MathDojo()
print(md3.add(1, 2, 3, 4).result)         
print(md3.subtract(1, 1).result)          
print(md3.add(10).result)                 

# FINAL CHAIN TEST 
md4 = MathDojo()
x = md4.add(2).add(2, 5, 1).subtract(3, 2).result
print(x) 