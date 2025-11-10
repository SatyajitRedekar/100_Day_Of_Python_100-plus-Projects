# todo dictionary comprehension
# comp_dict = {new_key:new_value for item in list}
# comp_dict = {new_key:new_value for (key,value) in dict.items()}

# todo conditional dictionary comprehension
# comp_dict = {new_key:new_value for (key,value) in dict.items if conditions}


# random score generate for the student
import random
names = ["Aarav","Isha","Rohan","Priya","Aditya","Neha"]
new_dict = {name : random.randint(1,100) for name in names}
print(new_dict)
passed_std = {name:score for (name,score) in new_dict.items() if score > 60}
print(passed_std)
