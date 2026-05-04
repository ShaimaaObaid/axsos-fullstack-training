#rock paper scissor game
import random
def get_choices():
  #player_choice = input("Enter a choice (rock,paper,scissor): ")
  options = ["rock","paper","scissor"]
  computer_choice = random.choice(options)
  #choices={"player":player_choice,"computer":computer_choice}
  
  #return choices
  
def check_win(player,computer):
  print(f"you chose {player} , computer chose {computer}")
  if player == computer:
   return "It's a tie!"
  elif player == "rock":
    if computer == "scissor":
      return "Rock smashes scissor! you win "
    else:
      return "paper covers rock! you lose"
  elif player == "paper":
    if computer == "scissor":
      return "scissor cuts paper! you lose "
    else:
      return "paper covers rock! you win"
  elif player == "scissor":
    if computer == "paper":
      return "scissor cuts paper! you win "
    else:
      return "rock smashes scissor! you lose"

choices = get_choices()
#result= check_win(choices["player"],choices["computer"])

#
name = "Shaymaa"
age = 23
float_num=float(5)
float_num1=5.5
print(name)
print(type(age))
print(type(age)== str)
print(isinstance(age,int))
print(isinstance(name,str))
print(isinstance(float_num,float))
print(isinstance(float_num1,float))

#operators = + - * / % ** // 
#4**2=16,5//2=2
age= 23
age+=23 #age=age+23
print(age)

#ternary operator
def is_adult(age):
  return True if age > 18 else False
#
name = "shaymaa"
name+= " is my name"
print(name)

print("""
      shaymaa
      and

      ali
""")
print("shaymaa".upper())
print(name) 
print("shayMAa".lower()) 
print("SHaymaa alI".title())
print("shaymaa".islower())
print("shaymaa".startswith("i"))
print("shaymaa".endswith("i"))
print("shaymaa".replace("s","a"))
print("shaymaa ali ahmed".split())
print("shaymaa ali ahmed".strip())
print("shaymaa".find("h"))
print("shaymaa".isalpha())
print(" ".isalpha())
print(len(name))#name = "shaymaa" name+= " is my name"=>shaymaa is my name
print("sh" in (name))
print("sq" in (name))
print("shay\"a")# using backslash
print("shaymaa \nali")
print(name[1])
print(name[-1])
print(name[1:5])
print(name[:9])

done = False
if done:# if true
  print("yes")
else:#false
  print("no")
#number are always true except 0
done=0  # zero mean false and all remain numbers are true
if done:
  print("yes")
else:
  print("no")
# string are false when empty string like ""
#check is done is boolean
done = False
print(type(done) == bool)

#any function
read_book = True
read_book2 = False
#return true if any of the values is true
read_any_book = any( [read_book,read_book2])
print(read_any_book)
#return true if all the values are true
read_all_book = all ( [read_book,read_book2])
print(read_all_book)
#complex numbers
num1 = 2+3j
num2 = complex(2,3)
print(num2.real,num2.imag)
#built-in fun
print(abs(5.5))
print(abs(-5.5))
print(round(5.5))
print(round(5.49))
print(round(-5.5))
#user input
#age = input("what is your age? ")
#print("your age is: "+age)
#control statement
condition = True
name="roger"
if condition == True :
  print("The condition")#indentation 2 or 4 spaces
  print("was true")
elif name=="roger":
  print("hello roger")
elif name=="mona":
  print("hello mona")
else:
    print("The condition")#indentation 2 or 4 spaces
    print("was false")

print("outside if")

#lists
dogs = ["Roger",1,"syd",True]
empty_list = []
print("Roger" in dogs)
print(dogs[0])
empty_list.append("shaymaa")
empty_list.extend(["aya"])
empty_list.extend(["maiar","mariam"])
girls = ["girl1","girl2"]
girls += ["girl3","girl4",5]
print(empty_list)
print(empty_list[-1])
print(dogs[-2])
print(dogs[0:2])
print(dogs[2:])
print(len(dogs))
girls.remove(5)
print(girls.pop())
print(girls)
items = [1,2,3,4,5,6]
items.insert(2,"tea")
print(items)
items[1:1]=["Pablo","laura"]
print(items)
string_list = ["aa","cc","bb","ff","dd","AA","MM","FF"]
#sort the upper first the lower
string_list.sort()
print(string_list)
#sort not caring about lower or upper
string_list.sort(key=str.lower)
print(string_list)
#or just we can use sorted
print(sorted(string_list,key=str.lower))

#tuples=> imutaple => we can not remove or add items
names = ("roger","syd")
print(names[-1])
print(names.index("roger"))
print(len(names))
print(1 in names)
print(names[0:1])
new_tuple = names + ("tina" , "Quincy")
print(new_tuple)
#dictionaries
dog = {"name":"Roger", "age": 8}
dog["name"] = "syd"
print(dog["name"])
print(dog.get("name"))
print(dog.get("color"))
print(dog.get("color","brown"))
print(dog.pop('name'))
print(dog)
cat ={"name":"cat","age":"2","color":"white"}
print(cat.popitem())
print("color" in cat)
print(cat)
print(cat.keys())
print(list(cat.keys()))
print(list(cat.values()))
print(list(cat.items()))
print(len(cat))
cat["favorite food"] = "meat"
print(cat)
del cat["age"]
print(cat)

#sets not ordered and immutaple
#we do not have the same item in set
#if we add "syd" to the set1 and print it like print(set1)we will have {'syd', 'Roger'}
set1 = {"Roger","syd"}
set2 = {"Roger"}
intersect = set1 & set2
print(intersect)
Union = set1 | set2
print(Union)
difference = set1 - set2
print(difference)
mod = set1 > set2
print(mod)
print(list(set1))

#function
def hello(name = "my friend",age=23):
  print("hello "+name +" you are "+str(age) +" years old")
hello("david",39)  
#hello() this will give an error there is no argument if we have not add an default value
hello()
def change(value):
  value=2
val = 1
change(val)
print(val)
#dictionary is mutpale
def change(value):
  value["name"]="syd"
val = {"name":"beau"}
change(val)
print(val)
#fun can return value
def hello(name):
  if not name:
    return
  print("Hello "+name+"!")
hello(False) #will apply the return and do not print 
hello("Shaymaa")
# when it return
def hello(name):
  print("Hello "+name+"!")
  return name, "ahmed",8
hello("syd")# no return
print(hello("syd"))

#variable scope
age = 8 #global var 
def test():
  age = 3 #local var available inside the fun
  print(age)
print(age) # if there is no global fun will give an error
test() #if there is no local var it will print 8 

#nested functions
def talk(phrase):
  def say(word):
    print(word)
  
  words = phrase.split(" ")#["i","am".....]
  for word in words:
    say(word)# will enter the say function above and print (word)
talk("I am going to buy the milk") 

def count():
  count = 0
  def increment():
    nonlocal count # if we want  to access a var that defined the outer fun from the inner fun
    #we first need to declare it as nonlocal 
    count = count + 1
    print(count)
  increment()
count()    
#objects
items = [1,2]
items.append(3)
print(items)
items.pop()
print(items)
#loops
condition = True
while condition == True:
  print("the condition is true")
  condition = False

count = 0
while count < 10:
  print("the condition is true")
  count+= 1
print("After the loop") 

items = [1,2,3,4]
for item in items :
  print(item)

for item in range(10):
  print(item)

items = ["shaymaa","aya","mariam"]
for index, item in enumerate(items):
  print(index,item)
#continue
items = [1,2,3,4]
for item in items:
  if item == 2:
    continue
  print(item)#1 3 4

#break
items = [1,2,3,4]
for item in items:
  if item == 2:
    break
  print(item)# 1

#classes
class Animal:
  def walk(self):
    print("walking ...")

class Dog(Animal):
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def bark(self):
    print("woof!")

roger= Dog("roger",8)
print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
#inheritance
roger.walk()


#modules every py file is a module
#we can do this
import math
print(math.sqrt(4))
#or this
from math import sqrt
print(sqrt(4))

#lambda functions
#lambda#arg  : #expression
lambda num : num *2
#assign lambda fun to the multiply var
multiply = lambda a,b : a * b
print(multiply(2,4))

#map(),filter(),reduce()(python provides 3 useful global fun we can use to work with collections)
#map()
numbers = [1,2,3]
def double (a):
  return a * 2

result = map(double,numbers)
print(list(result))
#using lambda function
numbers = [1,2,3]
double = lambda a :a * 2

result = map(double,numbers)
print(list(result))

#or just like this without assign lambda to the var
numbers = [1,2,3]
result = map(lambda a :a * 2,numbers)
print(list(result))

#filter
numbers = [1,2,3,4,5,6,7,8]
def isEven(n):
  return n % 2 == 0
result = filter (isEven,numbers)
print(list(result))
#using lambda fun with filter
numbers = [1,2,3,4,5,6,7,8]
result = filter (lambda n :n % 2 == 0,numbers)
print(list(result))
# without reduce 
expenses =[
  ("dinner", 80),
  ("car repair",120)
]
sum = 0
for expense in expenses :
  sum +=expense[1]
print(sum)
#using reduce and lambda
from functools import reduce
expenses =[
  ("dinner", 80),
  ("car repair",120)
] 
sum = reduce(lambda a,b : a[1]+b[1],expenses)
print(sum)

#recursion 
def factorial(n):
  if n == 1 : return 1
  return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

#decorators
def logtime(func):
  def wrapper():
    print("before")
    val = func()
    print("after")
    return val
  return wrapper
@logtime
def hello():
  print("hello")
hello()
#Docstrings """ """
def increment(n):
  """Increment a number"""
  return n + 1
class dog :
  """A class representing a dog"""
  def __init__(self,name,age):
    """initialize a new dog"""
    self.name = name
    self.age = age

  def bark(self):
    """let the dog bark"""
    print("woof!")
print(help(dog))

#without Annotations
def increment(n):
  return n + 1
count = 0
#with annotation 
def increment(n : int)->int:
  return n+ 1
count : int = 0

#exceptions
try:
  result = 2 / 0
except ZeroDivisionError:
  print("can not divided by zero!")
finally:
  result = 1

print(result)
# the original way using for 
numbers = [1,2,3,4,5]
numbers_power_2 = []
for n in numbers:
 numbers_power_2.append(n**2)
print(numbers_power_2)
#list compression
numbers = [1,2,3,4,5]
numbers_power_2 =[n**2 for n in numbers]
print(numbers_power_2)
#using lambda
numbers = [1,2,3,4,5]
print(list(map(lambda n : n**2 ,numbers)))

#polymorphism generalize a functionality so we can work on different types
class dog:
  def eat (self):
    print("Eating dog food")

class cat:
  def eat (self):
    print("Eating cat food")
#we defined same method eat()in different classes
#direct
dog().eat()
#or generate obj and call the eat method
animal2 = cat()
animal2.eat()


#operator overloading
#make classes comparable and make them work with python operator
class dog:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __gt__(self, other):
    return True if self.age > other.age else False

roger = dog("roger",8)
syd = dog("syd",7)
print(roger > syd)

#
import random
cards =[]
ranks = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits =["spades","clubs","hearts","diamonds"]

for suit in suits:
  for rank in ranks:
   cards.append([suit,rank])
def shuffle():
  random.shuffle(cards)
def deal(number):
  cards_dealt = []
  for x in range(number):
    card = cards.pop()
    cards_dealt.append(card)
  return cards_dealt
shuffle()  
cards_dealt =deal(2)
card = cards_dealt[0]
rank = card[1]
if rank == "A":
  value = 11
elif rank == "J" or rank == "Q" or rank == "K":
  value = 10
else:
  value = rank

rank_dict = {"rank": rank , "value": value}
print(rank_dict["rank"],rank_dict["value"])
