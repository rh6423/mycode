#!/usr/bin/env python3
# script to map percentage grades to letter
score = int(input('What is your numeric score? '))
# reject score > 100
if score > 100:
    print("scores greater than 100 don't get a letter, sorry")
    exit()
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
message = 'A score of ' + str(score) + ' equals a grade of ' + grade
print(message)
