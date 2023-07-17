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

sum = 0
print("=" * 50)
print("Index\t\tName\t\tGPA")
print("=" * 50)
for n in range(len(student)):
    print(f"{n + 1}\t\t{student[n]}\t\t{gpa[n]}")
    sum += gpa[n]
        
# for n in range(len(student)):
#     gpa = float(input(f"{n + 1} {subjects[n]} gpa is : "))
#     sum += gpa

avg_gpa = sum / len(student)
print("=" * 50)
print("average : {:.2f}".format(avg_gpa))
print("=" * 50)


