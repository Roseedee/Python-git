
############# exp define list ################
# list1 = [12, 12, 12] #int
# list2 = [12.2, 12.3, 12.4] #float or double
# list3 = ["12.5", "asdf", "12"] #string 
# list4 = ["12.5", 12, 1.2]

# print(type(list4[2]))

# test1
##############################################

score = [2, 4, 8, 1, 9, 3]

sum_score = 0
min, max = score[0], score[0]

for n in score:
    sum_score += n
    if min > n:
        min = n
    if max < n:
        max = n

avg_score = sum_score / len(score)
    
print("sum score is : ", sum_score)
print("average score is : ", avg_score)
print("min score is : ", min)
print("max score is : ", max)
