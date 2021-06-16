class ATM():
    def __init__(self, userName, cardNo, pinNo, balance,):
        self.userName = userName
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.balance = balance

    def getBalance(self):
        print(User.balance)
    
Name = input('Enter Name: ')
Card = input('Enter Card Number: ')
Pin = input('Enter Your Pin: ')
Balance = int(input('Balance You Want In Your Account: '))

User = ATM(Name, Card, Pin, Balance)

print('Type: "checkBalance" To Check Balance In Your Account.')
print('Type: "userInfo" To Check All Information About User.')
print('Type: "withdraw" To Withdraw Money From Your Bank Account.')

command = input('What Do you want Us To Do?: ')

if(command == 'checkBalance'):
    print(User.getBalance)

if(command == 'withdraw'):
    amount = int(input('Enter Amount You Want To Withdraw: '))
    cardPin = input('Enter Your Card Number: ')
    pinNum = input('Enter Your Pin: ')
    count = 0


    if(amount > User.balance):
        print("You Don't Have Enough Money In Your Account")
    else:
        count = count+1
    
    if(cardPin != User.cardNo):
        print("Card Number Donsn't Matched!")
    else:
        count = count+1

    if(pinNum != User.pinNo):
        print("Pin Dosen't Matched!")
    else:
        count = count+1

    if(count == 3):
        print('Transaction Done!')
        finalAmount = User.balance - amount
        finalAmount = str(finalAmount)
        print("Your Current Balance: "+finalAmount)


    else:
        print('Failed To Do Transaction')

if(command == "userInfo"):
    print('Name: '+User.userName)
    print('Card No: '+User.cardNo)
    print('Pin No: '+User.pinNo)
    bal = str(User.balance)
    print('Balance: '+bal)