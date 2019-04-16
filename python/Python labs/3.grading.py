#3.grading.py
grade = int(input('What is the grade?  '))

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade ='F'

one_unit = grade % 10
if letter_grade != 'F':
    if one_unit >= 7:
        sign = '+'
    elif one_unit <= 3:
        sign = '-'
    else:
        sign = ''
print(str(letter_grade) + sign)
