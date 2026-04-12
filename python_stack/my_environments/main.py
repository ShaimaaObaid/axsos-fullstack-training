print("hello world")
name="ali"
#not firstName it is first_name with underline
first_name="Shaymaa"
last_name="Obaid"
print(first_name+last_name)

x=5
y=7
print(x+y)
print(y/x)
print(y//x)
# false and true first letter should be capital False,True
is_married= False
is_logged= True
#lists/sets/tuple
inventory=["chair","desk","pen"]
inventory.append("mouse")
print(inventory)
print(inventory[0])
inventory[0]="book"
print(inventory)
inventory.pop()
print(inventory)
inventory.pop(1)
print(inventory)



#immutable cannot be changed after creating
closed_inventory=('t-shirt','trousers','jeans','shorts')
print(closed_inventory)
print(closed_inventory[0])
#closed_inventory[1]="shirt" error cannot be change after creating
age=30
print("my age is "+str(age))
print(f"my age is {age}")
print("my age is {} {}".format(age,first_name))
#
my_dict={
    "phone":"iphone 14",
    "mouse":"dell",
    "light":"table lamp"

}
print(my_dict["phone"])
for i in my_dict:
    print(i)
for key in my_dict.keys():
    print(key)
for key in my_dict:
    print(my_dict[key])
for key,value in my_dict.items():
   print(value)
my_dict['phone']="samsung"
print(my_dict)
my_dict['book']=['novel','essay']
print(my_dict)
z=my_dict.pop('book')
print(z)
print(my_dict)
print(type('book'))
print(type(my_dict))
print(len(my_dict))

#for
my_list=[1,2,3,4]
#(start,stop,change)
for i in range(0,4,1):
    print(i)
for i in range(4,0,-1):
    print(i)
for i in range(0,len(my_list),1):
    print(i)
print(len(my_list))
my_items=["charger","phone","headphone"]

for i in range(0,len(my_items),1):
    print(my_items[i])
for i in range(len(my_items)-1,-1,-1):
    print(my_items[i])
for item in my_items:
    print(item)

x=6
if x==4:
    print(True)
elif x==6:
    print("x equals six")
else :
    print("x does not equal six or four ")
y=3
if y!=5:
    print(False)
is_not_married=True
is_logged=False 
if is_not_married or is_logged:
    print("you are not married or logged in ")

is_engaged=True
if is_engaged is not False:
    print("she is engaged") 
#methods in python , function in js
def sum(num1,num2):
   if num1 ==2:
       return #with writing return None or not the same
   return num1+num2
print(sum(2,3))
print("Hello World!")
x = "Hello Python"
print(x)

y = 42
print(y)
name="zeen"
print("my name is",name)
print("my name is "+name)
age=13
print("my age is",age)
print("my age is",str(age))
first_name="shaymaa"
last_name="obaid"
age=23
print(f"my name is {first_name} {last_name} and my age is {age}")
print("my name is {} {} and my age is {}".format(first_name,last_name,age))
hw="hello %s" %"world"
py="i love python %d"%3
print(hw,py)
print("my name is %s and my age is %d"%(first_name,age))
y="hello world"
print(y.title())
print(y.upper())
print(y.lower())
print(y.count("l"))
print(y.split("l"))
print(y.find("o"))
print(y.isalnum())
print(y.isalpha())
print(y.isdigit())
print(y.islower())
print(y.isupper())
print(y.endswith("d"))
print(y.endswith("o"))
x=10
if x>10:
    print("x is bigger than 10")
elif x==10:
    print("x=10")
else:
    print("x small than 10")

class EmptyClass:
    pass # pass for no error like null
my_string=""
for value in my_string:
    pass # nothing happen but it can be useful in places where your code has not been completed yet.
total=35
user_value="24"
#total=total+user_value   will give an error
total=total+int(user_value)
print(total)

for x in range(0,10,1):
    print(x)
for x in range(0,10): #without+1
    pass
for x in range(10):#without+1 or 0 already start from 0
    pass


for count in range(0,5):
    print("looping - ", count)
