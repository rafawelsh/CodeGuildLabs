#11.simple_calc.py
while True:
    oper = input('What is the operation you\'d like to perform? ').lower()
    if oper == 'done':
        break
    else:
        pass

    x1 = float(input('What is number 1? '))
    x2 = float(input('What is number 2? '))

    if oper in ['+', 'add', 'sum']:
        oper = '+'
        result = x1 + x2
    elif oper in ['-', 'subtract', 'minus']:
        oper = '-'
        result = x1 - x2
    elif oper in ['*', 'multiply', 'times']:
        oper = '*'
        result = x1 * x2
    elif oper in ['/', 'divide', 'div']:
        oper = '/'
        result = x1 / x2
    else:
        print("Put some numbers in!")
        continue

    print(f'{x1} {oper} {x2} = {result}')

print(eval('1*2'))

# operation = x1 * x2
# print(x1)
# print(x2)
# print(oper)
