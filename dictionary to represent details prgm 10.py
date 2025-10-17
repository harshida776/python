student = {
    "name": "Akash",
    "roll_number": 23,
    "register_number": "2025CS101",
    "department": "CSE",
    "semester": 5
}
student["total_mark"] = int(input("Enter total mark: "))

mark = student["total_mark"]

if mark >= 90:
    grade = "A"
elif mark >= 82:
    grade = "B"
elif mark >= 75:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark >= 50:
    grade = "P"
else:
    grade = "Fail"

student["grade"] = grade

del student["roll_number"]

print("\nStudent Details:")
print(student)
