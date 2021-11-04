# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# reading from csv
# import csv
#
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
# # pandas library
import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # convert to dictionary
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # convert to list
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # find the average temperature
# print(data["temp"].mean())
#
# find the maximum temperature
# print(data["temp"].max())

# # get data in columns
# print(data["condition"])
# print(data.condition)
# print(data.day)
# print(data.temp)

# get data in rows
# print(data[data.temp == data.temp.max()])
#
# # convert C to F -> formula = (0°C × 9/5) + 32
# monday = data[data.day == "Monday"]
# print(monday.temp)
# monday_temp_in_F = (int(monday.temp) * 9/5) + 32
# print(monday_temp_in_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
