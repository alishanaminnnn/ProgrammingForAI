registered = ["Ayesha", "Bilal", "Hina", "Usman", "Fatima", "Omar",
              "Zain", "Sana"]

day1 = ["Ayesha", "Bilal", "Hina", "Bilal", "Usman", "Fatima", "Hina"]
day2 = ["Hina", "Omar", "Ayesha", "Omar", "Zain", "Fatima"]

# Count total sign-ins
print("The number of sign-ins at Day1:", len(day1))
print("The number of sign-ins at Day2:", len(day2))

# Convert lists to sets to remove duplicates
day1 = set(day1)
day2 = set(day2)

print("The number of unique attendees at Day1:", len(day1))
print("The number of unique attendees at Day2:", len(day2))

# Find participants who attended both days
print("The certificate will be given to:", day1 & day2)

# Find participants who attended only one day
print("The participants who attended only one day:", day1 - day2, day2 - day1)

# Find registered participants who never attended
registered = set(registered)
print("Participants who never attended:", registered - (day1 | day2))

# Calculate the percentage who attended only one day
counter = 0
for i in (day1 - day2) | (day2 - day1):
    counter = counter + 1

print("Percentage:", (counter / len(registered)) * 100)

# Sort and print attendees alphabetically
day1 = sorted(day1)
print("Day 1:", day1)

day2 = sorted(day2)
print("Day 2:", day2)
