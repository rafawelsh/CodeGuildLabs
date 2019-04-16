# 20.creditcardvalidation.py
4556737586899855
card = list(input('Enter your credit card '))
validation = card.pop()
card = card[::-1]
print(card)
print()

index = 0
sum = 0
for j in card:
    if index%2 == 0:
        card[index] = int(j) * 2

    if int(card[index]) > 9:
        card[index] = int(card[index]) - 9

    sum += int(card[index])
    index += 1

number = str(sum)

if number[1] == validation:
    print('Valid!'')
