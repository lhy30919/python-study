marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d 번 학생: 합격" % number)
    else:
        print("%d 번 학생: 불합격" % number)

### for continue ###
# marks = [90, 25, 67, 45, 80]
#
# number = 0
# for mark in marks:
#     number += 1
#     if mark < 60: continue
#     print("%d 번 학생: 합격" % number)


### for continue range ###
# marks = [90, 25, 67, 45, 80]
#
# for number in range(len(marks)):
#     if marks[number] < 60: continue
#     print("%d 번 학생: 합격" % (number+1))