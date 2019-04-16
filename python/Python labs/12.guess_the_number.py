#12.guess_the_number.py
import random

x = random.randint(1,10)
i = 0
print(x)
last_guess = 0
while True:
    i += 1
    current_guess = int(input("guess the number: "))
    if current_guess == x:
        print('Yay!')
        print(f'It took you {i} guesses')
        break
    elif current_guess > x:
        print('Too high')
        distance_last = abs(last_guess - x)
        distance_current = abs(current - x)
        #lg = abs(last_guess - current_guess)
    else:
        print('Too low!')
    last_guess = current_guess

print(last_guess)

print(lg)

# import random
#
# x = random.randint(1,10)
# i = 0
# print(x)
#
# while True:
#     i += 1
#     guess = int(input("guess the number: "))
#     if guess == x:
#         print('Yay!')
#         print(f'It took you {i} guesses')
#     elif guess > x:
#         print('Too high')
#
#     else:
#         print('Too low!')
#
