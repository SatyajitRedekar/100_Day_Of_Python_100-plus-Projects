# TODO this out put needed an cleaning process
print("\nthis is an traditional method for the csv")
with open("weather_data.csv") as data:
    content = data.readlines()
    print(content)
    "\n"

# TODO this is an advanced feature that provided by python for handling the csv
import csv
print("\nthis is using import csv pip")
with open("weather_data.csv") as data:
    content = csv.reader(data)
    for x in content:
        print(x)
    # print(content)  this will return the file objects
    temperature = []
    for row in content:
        if row[1] != "temp" :
            temperature.append(row[1])
    print(temperature)
    "\n"

# todo : this this the most advanced way to work with csv that is pandas lib
import pandas as pd
print("\nthis using pandas lib")
cont = pd.read_csv("weather_data.csv")
print(cont)
print(cont["temp"])