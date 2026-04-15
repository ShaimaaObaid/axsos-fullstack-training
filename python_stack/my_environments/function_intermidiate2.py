x = [[5, 2, 3], [10, 8, 9]]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x': 10, 'y': 20}]

# 1) Update values

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

# 2) Iterate dictionary list

def iterateDictionary(some_list):
    for item in some_list:
        result = ""
        for key in item:
            result += f"{key} - {item[key]}, "
        print(result.rstrip(", "))

# 3) Get values from key

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
    

# 4) Dictionary with list values

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for value in some_dict[key]:
            print(value)

# TESTS

iterateDictionary(students)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
printInfo(sports_directory)