
marks = {"Ali": 85, "Sara": 92, "Hamza": 67, "Zara": 74, "Omar": 49,
         "Hina": 91, "Usman": 45}


# Return grade according to marks
def grade(m):
    if m >= 85:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 50:
        return "C"
    else:
        return "F"


# Display original results
print("----RESULT----")
count = 0

for i, j in marks.items():
    print("Name:", i)
    print("Marks:", j)
    print("Grade:", grade(j))

    if grade(j) != 'F':
        count = count + 1
    print()

# Calculate pass percentage
print("Pass Percentage:", (count / len(marks)) * 100)

# Add 3 marks to Omar's score
marks["Omar"] = marks["Omar"] + 3
print("New Marks:", marks["Omar"])

# Display updated results
print("----UPDATED-RESULT----")
count = 0

for i, j in marks.items():
    print("Name:", i)
    print("Marks:", j)
    print("Grade:", grade(j))

    if grade(j) != 'F':
        count = count + 1
    print()
