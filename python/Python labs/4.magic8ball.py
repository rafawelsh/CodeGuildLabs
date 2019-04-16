#4.magic8ball.py
import random

possible_answers = ('It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Reply hazy try again', 'Ask again later','Don't count on it', 'My reply is no', 'My sources say no' , 'Outlook not so good', 'Very doubtful')

while True:

    input('Welcome to the all knowing Orb. Ask a question and I will answer it! > ')

    print(random.choice(possible_answers))

    input('Would you like to ask another question? > ')

    if input == ('yes'):
        print('Good')
    else:
        print('Good bye')
    break
