import random
def randInt(min=0, max=100):

    if min > max:
        min, max = max, min

    if max < 0:
        max = 0

    if min < 0:
        min = 0

    return int(random.random() * (max - min + 1)) + min

print(randInt())             
print(randInt(max=50))        
print(randInt(min=50))        
print(randInt(min=50, max=500))  