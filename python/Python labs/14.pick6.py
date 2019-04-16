#14.pick6.py
import random


def pick6(tempmoney):
    match = []
    wins = 0
    tempmoney -= 2
    lottery = [random.randint(1,99) for n in range(6)]
    user_nums = [random.randint(1,99) for n in range(6)]
    # print("lottery numbers: %s" % lottery)
    # print("user numbers: %s" % user_nums)

    for n in range(len(lottery)):
        if user_nums[n] == lottery[n]:
            match.append(n)

    if len(match) == 1:
        tempmoney += 4
    elif len(match) == 2:
        tempmoney += 7
    elif len(match) == 3:
        tempmoney += 100
    elif len(match) == 4:
        tempmoney += 50000
    elif len(match) == 5:
        tempmoney += 1000000
    elif len(match) == 6:
        tempmoney += 25000000

    print(tempmoney)
    # print(match)
    return tempmoney

def main():
    replay = True

    print('*' * 60)
    print('Welcome to Pick6!')
    print('*' * 60)
    while replay:
        i = 0
        money = 0
        reply = input('Ready to play 100,000 times?: ').strip().lower()

        while i < 1000000:
            if reply.startswith('y'):
                # print('main before pick6 func ' + str(money))
                money = pick6(money)
                # print('main after pick6 ' + str(money))
                # balance()
                i += 1
            else:
                print('You sure?')  #NEED TO FIX THIS PART.
                break

        while True: # input validation
            play_again = input('Do you want to play again: ').strip().lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                break

        if play_again.startswith('n'):
            replay = False
            print('-'*60)
            print('Goodbye!')
            print('-'*60)

if __name__ == '__main__':
    main()

# pick6()
