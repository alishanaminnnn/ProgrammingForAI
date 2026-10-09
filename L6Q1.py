readings = [("Mon", 31.5), ("Tue", 34.0), ("Wed", 29.5), ("Thu", 36.5),
            ("Fri", 36.5), ("Sat", 33.0), ("Sun", 30.0)]

# Calculate average temperature
total = 0
for days, temp in readings:
    total = total + temp

days = len(readings)
average_temp = total / days
print("Average Temperature:", average_temp)

# Find the maximum temperature
maximum = readings[0][1]
for days, temp in readings:
    if temp > maximum:
        maximum = temp

print("1. The maximum temperature is:", maximum)

# Print days with the highest temperature
print("2. Days with the hottest temperature:")
for days, temp in readings:
    if temp == maximum:
        print(days)

# Find days with above-average temperatures
above_average = []
for days, temp in readings:
    if temp > average_temp:
        above_average.append(days)

print("Days with above average temperature:")
print(above_average)

# Sort temperatures in descending order
temperatures = []
for days, temp in readings:
    temperatures.append(temp)

temperatures.sort(reverse=True)
print(temperatures)

# Print the last three days' readings
print("The last 3 days' readings:")
print(readings[-3:])


