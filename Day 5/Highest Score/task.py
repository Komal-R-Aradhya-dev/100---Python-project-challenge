student_scores = [ 150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 19, 78, 65, 89, 86, 55, 91, 64, 89150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 19, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
# sum_ = 0
# for i in student_scores:
#     sum_ += i
# print (sum_)
# t_score = sum(student_scores)
# print(t_score)
# print(max(student_scores))
# print(min(student_scores))
Max = 0
for i in student_scores:
    if i >Max :
        Max = i
print (Max)
Min = 100
for i in student_scores:
    if i < Min :
        Min = i
print (Min)

