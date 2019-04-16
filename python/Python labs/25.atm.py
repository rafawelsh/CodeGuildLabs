# 25.atm.py

class ATM():
    '''Creating the account of the user.'''
    def __init__(self, name=None, balance=0.0, transactions=[]):
        self.name = name
        self.balance = balance
        self.transactions = transactions


    '''Checking the available balance on the user's account'''
    def check_balance(self):
        return f'Your balance is ${self.balance}'

    '''Depostiing money into account, only positive values'''
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposit: ${amount}')
        print(f'Your balance is ${self.balance}')

    '''Checking balance to see if whitdrawal amount is possible'''
    def check_withdraw(self, amount):
        return amount <= self.balance

    '''Withdrawing the amount from the balance and returning remaining balance'''
    def withdraw(self, amount):
        if self.check_withdraw(amount):
            self.balance -= amount
            self.transactions.append(f'Withdraw: ${amount}')
            print(f'You withdrew ${amount}.')
        else:
            print('You do not have the funds.')


    def print_transactions(self):
        print('-'*10)
        for transaction in self.transactions:
            print(transaction)
        print('-'*10)


def main():
    atm = ATM()
    loop = True
    valid_inputs = [0, 1, 2, 3, 4, 5]
    commands = '''
    What would you like to do today?
    [0] Deposit
    [1] Withdraw
    [2] Check balance
    [3] History
    [4] Commands
    [5] Exit
    '''

    print('Welcome')
    while loop:
        valid = False

        while not valid:
          print(commands)
          cmd = int(input('> ').strip().lower())
          if cmd in valid_inputs:
              valid = True
          else:
              print('Choose Valid Option')
              print(commands)

          if cmd in [0, 'd', 'deposit']:
            print('*' *10)
            amount = int(input('How much would you like to deposit? '))
            atm.deposit(amount)
            print('*' *10)

          elif cmd in [1, 'w', 'withdraw']:
            print('*' *10)
            amount = int(input('How much would you like to withdraw? '))
            atm.withdraw(amount)
            print('*' *10)

          elif cmd in [2, 'check', 'check balance']:
            print('*' *10)
            print(atm.check_balance())
            print('*' *10)

          elif cmd in [3, 'h', 'history']:
            print('*' *10)
            print('Transaction History')
            if len(atm.transactions) > 0:
                atm.print_transactions()
            print('*' *10)

          elif cmd in [4, 'commands']:
            print('*' *10)
            print(commands)
            print('*' *10)

          elif cmd in [5, 'e', 'exit']:
            loop = False
            print('*' *10)
            print('Goodbye!')
            print('*' *10)
            pass

if __name__ == '__main__':
    main()
