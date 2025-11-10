student_dict = {
    "student" : ["satyajit","krishna","radha"],
    "score" : [90,100,80]
}

# Looping through dictionaries:
for (key , value) in student_dict.items():
    print(key , value)

# Going through pandas dataFrame
import pandas
pandas_dict = pandas.DataFrame(student_dict)
print(pandas_dict)

for (key,value) in pandas_dict.items():
    print(value)

# Looping through row of dataFrame
for (index,row) in pandas_dict.iterrows():
    print(index)
    print(row)