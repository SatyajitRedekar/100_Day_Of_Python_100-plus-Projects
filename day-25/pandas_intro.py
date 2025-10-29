import pandas
import pandas as pd

data = pd.read_csv("weather_data.csv")

print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# todo calculate an average of temperature
average = sum(temp_list) / len(temp_list)
print(average)

# using the pandas
average = data["temp"].mean()
print(average)

max_temp = data["temp"].max()
print(max_temp)

# getting a column data
print(data["condition"]) # this is calling like dict
print(data.condition) # data frame treated like attribute

# getting a row of data
print(data[data.day == "Monday"]) # data.day = data["data"]

# printing max temp day
print(data[data.temp == data.temp.max()])

# converting mondays temp Celsius to Fahrenheit
monday_temp = data[data.day == "Monday"]["temp"]
print((monday_temp * 9/5) + 32)

# create a data fream from scratch
data_dictionary = {
    "student" : ["Amy","James","Angela"],
    "scores" : [76, 56, 65]
}

data_panda = pandas.DataFrame(data_dictionary)
data_panda.to_csv("new_data")