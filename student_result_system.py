n = int(input("Enter number of students: "))

students = {}
total = 0

a_count = b_count = c_count = fail_count = 0
passed = []
failed = []

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    total += marks

# topper
topper_name = max(students, key=students.get)
topper_marks = students[topper_name]

# average
avg = total / n

# grade distribution
for name, marks in students.items():
    if marks >= 90:
        a_count += 1
        passed.append(name)
    elif marks >= 75:
        b_count += 1
        passed.append(name)
    elif marks >= 50:
        c_count += 1
        passed.append(name)
    else:
        fail_count += 1
        failed.append(name)

print("\n------ RESULT ------")
for name, marks in students.items():
    print(name, "=", marks)

print("Topper =", topper_name, "(", topper_marks, ")")
print("Average =", avg)

print("\nGrade Distribution")
print("A Grade =", a_count)
print("B Grade =", b_count)
print("C Grade =", c_count)
print("Fail =", fail_count)

print("Passed Students =", passed)
print("Failed Students =", failed)

print("Topper Percentage =", topper_marks, "%")
# search by name
search_name = input("\nEnter student name to search: ")

if search_name in students:
    print(search_name, "=", students[search_name])
else:
    print("Student not found")
