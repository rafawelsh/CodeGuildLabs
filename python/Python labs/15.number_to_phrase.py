# 15.number_to_phrase.py

ones_digit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
              7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirty', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
               19: 'nineteen'}
tens_digit = {2: 'twenty', 3: 'thirties', 4: 'forty', 5: 'fifty', 6: 'sixty',
              7: 'seventy', 8: 'eighty', 9: 'ninety'}
# ones
nums = int(input('What number would you like to make a phrase?: '))


def phrase(nums):
    tens = nums//10
    single = nums%10


    if 99 >= nums >= 20:
        if single == 0:
            return tens_digit[tens]
        else:
            return (f'{tens_digit[tens]}-{ones_digit[single]}')

    if nums <= 20:
        if 20 > nums >= 10:
            return ones_digit[nums]
        else:
            return ones_digit[single]


print(phrase(9))
print(phrase(10))
print(phrase(15))
print(phrase(19))
print(phrase(20))
print(phrase(55))
