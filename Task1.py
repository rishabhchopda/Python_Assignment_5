student_details = {"Rishabh" : 85,
                   "Daxuu" : 90,
                   "XYZ" : 79,
                   "ABC" : 88}

student = input("Enter the student's name: ")

if student in student_details:
    print(f"{student} marks : {student_details[student]}")
else:
    print("Student not found.")