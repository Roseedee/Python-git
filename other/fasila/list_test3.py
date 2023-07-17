student = [
    "Olarik",
    "Kaveepoj",
    "Suwichai"
]

gpa = [
    3.5,
    3.9,
    3.2
]

while True:
    use_select = input("do you want to add new student(y[yes]/n[no]) : ")
    if use_select == "y" or use_select == 'Y' or use_select == "yes":
        st_name = input('Please Insert student name : ')
        st_gpa = float(input("Please Insert student gpa : "))
        student.append(st_name)
        gpa.append(st_gpa)
    else:
        break

sum = 0
print("=" * 50)
print("Index\t\tName\t\tGPA")
print("=" * 50)
for n in range(len(student)):
    print(f"{n + 1}\t\t{student[n]}\t\t{gpa[n]}")
    sum += gpa[n]

avg_gpa = sum / len(student)
print("=" * 50)
print("average : {:.2f}".format(avg_gpa))
print("=" * 50)
    
