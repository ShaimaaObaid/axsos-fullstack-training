#Biggie Size :Given a list, write a function that changes all positive numbers in the list to "big".
def Biggie_size(my_list):
    for i in range(len(my_list)):
        if my_list[i] >0:
            my_list[i]="big"
    return my_list
    
print(Biggie_size([-1,3,5,-5])) 
#Count Positives - Given a list of numbers, create a function to replace the last value with
# the number of positive values. (Note that zero is not considered to be a positive number)
def Count_positives(my_list):
    count=0
    for i in range(len(my_list)):
        if my_list[i]>0:
            count+=1
    if len(my_list)>0:
        my_list[-1]=count
    return my_list        
print(Count_positives([-1,1,1,1]))
print(Count_positives([1,6,-4,-2,-7,-2]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list
def total(my_list):
    sum_total=0
    for num in my_list:
        sum_total+=num
    return sum_total
print(total([1,2,3,4])) 
print(total([6,3,-2]))

#Average - Create a function that takes a list and returns the average of all the values.x
def average(my_list):
    if len(my_list) == 0:
        return 0
    total = 0
    for num in my_list:
        total += num
    return total / len(my_list)

print(average([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list
def length(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count

print(length([37,2,1,-9]))
print(length([]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
#  If the list is empty, have the function return False.
def minimum(my_list):
    if len(my_list) == 0:
        return False
    min_val = my_list[0]
    for num in my_list:
        if num < min_val:
            min_val = num
    return min_val

print(minimum([37,2,1,-9]))
print(minimum([]))

#Maximum - Create a function that takes a list and returns the maximum value in the list.
#  If the list is empty, have the function return False.
def maximum(my_list):
    if len(my_list) == 0:
        return False
    max_val = my_list[0]
    for num in my_list:
        if num > max_val:
            max_val = num
    return max_val

print(maximum([37,2,1,-9]))
print(maximum([]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has
#  the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(my_list):
    if len(my_list) == 0:
        return False
    
    total = 0
    min_val = my_list[0]
    max_val = my_list[0]
    count = 0

    for num in my_list:
        total += num
        count += 1
        
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    avg = total / count

    return {
        'sumTotal': total,
        'average': avg,
        'minimum': min_val,
        'maximum': max_val,
        'length': count
    }

print(ultimate_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed.
#  Do this without creating a second list.(This challenge is known to appear during basic technical interviews.)
def reverse(my_list):
    start = 0
    end = len(my_list) - 1

    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

    return my_list

print(reverse([37,2,1,-9]))