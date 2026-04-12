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
#immutable cannot be changed after creating
closed_inventory=('t-shirt','trousers','jeans','shorts')
print(closed_inventory)
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


