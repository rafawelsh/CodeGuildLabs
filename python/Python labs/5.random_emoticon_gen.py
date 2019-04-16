#5.random_emoticon_gen.py
import random

eyes = [':', ';', '=', 'X',]
noses = ['-', 'o','u','{']
mouths = [')', '(', 'D', 'p', '|']

i = 0
while i < 6:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    print(emoticon)
    i += 1
print('Here are 5 faces for ya!')
