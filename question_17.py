grades = {"John": 45, "Alice": 78, "Bob": 55}

print("Students who scored above 50:")
for student, score in grades.items():
    if score > 50:
        print(student)
