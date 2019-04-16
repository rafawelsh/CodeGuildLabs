#8.make_change.py
while True: #input validation

    cash = input("How many cash do you have? > ").strip().strip('$')
    # if cash[0] == '$':
    #     cash.pop(0)
    try:
        cash = round(float(cash) * 100)
        if cash < 0:
            raise ValueError
        break
    except ValueError:
        print('Please enter a number')

denomination = {
    'hundreds': 10000,
    'fifties': 5000,˜
    'twenties': 2000,
    'tens': 1000,
    'fives': 500,
    'ones': 100,
    'quarters': 25,
    'dimes': 10,
    'nickles': 5,
    'pennies': 1
}

change = ['Your change is']

for d in denomination:
    d_change = cash // denomination[d]
    cash %= denomination[d]
    change.append(f'{d_change} {d}')

print(', '.join(change))

#
# quarters = cash//25
# lo = cash%25
# dimes = lo//10
# lo = lo%10
# nickles = lo//5
# pennies = lo%5
#
#
# print("You have", quarters, "quarters")
# print("You have", dimes, "dimes")
# print("You have", nickles, "nickles")
# print("You have", pennies, "pennies")
