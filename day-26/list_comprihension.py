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