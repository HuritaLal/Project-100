class Atm:
    def __init__(self,card_number,pin):
        self.card_number = card_number
        self.pin = pin

    def check_balance(self):
        print("Your Balance is 1 Million")

    def withdrawal(self,amount):
        new_amount= 1000000-amount
        print("You have Withdrawn amount"+str(amount)+"Your remaining Balance is"+str(new_amount))
    
def main ():
    card=input("Insert your Card Number")
    pin=input("Enter your Pin Number")
    new_user=Atm(card,pin)
    print("Choose your Activity")
    print("1.Balance Enquiary  2.Withdrawal")
    activity=int(input("Enter the activity number"))
    
    if(activity==1):
        new_user.check_balance()

    elif(activity==2):
        amount=int(input("Enter the Amount"))
        new_user.withdrawal(amount)
    
    else:
        print("Enter a Valid Number")

if __name__=="__main__":
    main()

