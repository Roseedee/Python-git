n_subject = int(input("enter subject num : "))

sum_score = 0

for subject in range(n_subject):
    score = int(input(f"enter point subject[{subject + 1}] : "))
    sum_score += score

avg_score = sum_score / n_subject

print("your sum point : " , sum_score)
print("Your average point is : ", avg_score)