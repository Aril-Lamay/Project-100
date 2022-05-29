class Atm:
    def __init__(self,pin_no, card_no):
        self.pin_no = pin_no
        self.card_no = card_no

    def checkBalance(self):
        print("You balance is 140000")
    
    def withdrawal(self,amount):
        new_amount = 140000 - amount
        print("You have withdrawn "+ str(amount) )
        print("Your new balance is "+ str(new_amount) )
    
def main():
    card = input("Enter the card no. :- ")
    pin = input("Insert your pin :- ")

    new_user = Atm(pin, card)

    print("Choose your activity")
    print("1. Balance Enquiry 2. Withdrawal")
    activity = int(input("Enter the activity number : "))

    if activity == 1:
        new_user.checkBalance()
    elif activity == 2:
        withdraw_amount = int(input("Enter withdrawal amount : "))
        new_user.withdrawal(withdraw_amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()