# Initialized
pin = '1234'
account_balance = 50000
account_number = 4567893210


print('Welcome to Nameless And Useless ATM')
print('''1. Check balance
2. Withdraw money
3. Deposit money
''')

# what u want??
choice = input('Enter your what you want`: ')

# If the user chooses to check their balance
if choice == '1':
    # Ask the user to enter their PIN
    if input('Enter your pin: ') == pin:
        # If the PIN is correct, display the account balance
        print(f'You have ${account_balance} in your account.')
    else:
        # If the PIN is incorrect, display an error message
        print('You have entered the wrong pin.')

# If the user chooses to withdraw money
elif choice == '2':
   
    if input('Enter your pin: ') == pin:
        withdrawal_amount = int(input('Enter the amount you wish to withdraw: '))
        # Check if the withdrawal amount is less than or equal to the account balance
        if withdrawal_amount <= account_balance:
            # If the withdrawal amount is valid, subtract it from the account balance
            account_balance -= withdrawal_amount
            #a success message with the new balance
            print(f'You have withdrawn ${withdrawal_amount}. Your new balance is ${account_balance}.')
        else:
            # If the withdrawal amount is greater than the account balance, display an error message
            print('Insufficient funds.')
    else:
        print('You have entered the wrong pin.')

# If the user chooses to deposit money
elif choice == '3':
   
    if input('Enter your pin: ') == pin:
        # If the PIN is correct, ask the user to enter the deposit amount
        deposit_amount = int(input('Enter the amount you wish to deposit: '))
        # Add the deposit amount to the account balance
        account_balance += deposit_amount
        # Display a success message with the new balance
        print(f'You have deposited ${deposit_amount}. Your new balance is ${account_balance}.')
    else:
        print('You have entered the wrong pin.')