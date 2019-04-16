#madlibs.py
import random

def madlibs():
    while True:
        three_adj = input('Choose 3 adjectives. ').split(' ')
        three_noun = input('Give me three nouns. ').split(' ')
        three_names = input('Give me three names. ').split(' ')
        three_verbs = input('Give me three verbs. ').split(' ')

        r_adj = random.choice(three_adj)
        r_noun = random.choice(three_noun)
        r_names = random.choice(three_names)
        r_verbs = random.choice(three_verbs)

        read = input('Would you like to hear your stroy? > ').lower()

        if read == 'yes':
            print(f'{r_names} {r_noun} {r_adj} {r_noun} {r_verbs} ')

            again = input('Would you like to read the story again? ').lower()

            if again == 'yes':
                continue

            else:
                redo = input('Would you like to do another madlib?').lower()

                if redo == 'yes':
                    continue
                else:
                    print('Okay. Bye!')
                    break
        else:
            print('Okay. Bye!')
            break

if __name__ == '__main__':
madlib()
