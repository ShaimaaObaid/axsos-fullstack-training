#Countdown - Create a function that accepts a number as an input.
#  Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).
def countdown(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(5))

#Print and Return - Create a function that will receive a list with two numbers.
#  Print the first value and return the second.
def print_and_return(my_list):
    print(my_list[0])
    return my_list[1]

print(print_and_return([1,2]))

#First Plus Length - Create a function that accepts a list and
#  returns the sum of the first value in the list plus the list's length.
def first_plus_length(my_list):
    return my_list[0] + len(my_list)

print(first_plus_length([1,2,3,4,5]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing
#  only the values from the original list that are greater than its 2nd value.
#  Print how many values this is and then return the new list.
#  If the list has less than 2 elements, have the function return False
def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False
    
    result = []
    count = 0

    for val in my_list:
        if val > my_list[1]:
            result.append(val)
            count += 1

    print(count)
    return result

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#This Length, That Value - Write a function that accepts two integers as parameters:
#  size and value. The function should create and return a list whose length is equal
#  to the given size, and whose values are all the given value.
def length_and_value(size, value):
    result = []
    for i in range(size):
        result.append(value)
    return result

print(length_and_value(4,7))
print(length_and_value(6,2))