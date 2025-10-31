# new_list = [new_item for item in list]
# list name = [condition for x(variable) in list]

# without list comprehension
list_of_numbers  = [1,2,3,4,5]
new_list_of_numbers = []

for number in list_of_numbers:
    add_1 = number + 1
    new_list_of_numbers.append(add_1)
print(new_list_of_numbers)

# using list comprehension
comp_list = [num + 1 for num in list_of_numbers]
print(comp_list)

# list comprehension with string
name = "satyajit"
new_name = [letter for letter in name]
print(new_name)

# challenge
double_num_list = [num * 2 for num in range(1,5)]
print(double_num_list)

# todo the conditional comprehension list
# list = [variable(conditional) for x(variable) in list if test (condition)]
names = ["Aarav","Isha","Rohan","Priya","Aditya","Neha"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
