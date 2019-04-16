# 17.palindrome_and_anagram.py
def check_palidrome(word):
    """
    >>> check_palidrome('racecar')
    palidrome!
    """
    palidrome = word[::-1]
    if palidrome == word:
        return 'palidrome!'
    else:
        print('sorry, not a palidrome...')


def check_anagram(w1, w2):


    if w1 == w2:
        print('Anagrams!')
    else:
        print('sorry no anagrams...')

def main():
    while True:
        choice = input('Would you like to do an palidrome or anagram?: ').lower().strip()
        if choice in ['p', 'palidrome', 'a', 'anagram']:
            break
        else:
            print('Please choose an option')

    if choice in ['p', 'palidrome']:
        word = input('Check out if its a palidrome: ')
        print(check_palidrome(word))
    else:
        w1 = sorted(input('word 1: ').lower().replace(' ',''))
        w2 = sorted(input('word 2: ').lower().replace(' ',''))
        check_anagram(w1, w2)

if __name__ == '__main__':
    main()
