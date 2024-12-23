class atm:
    def __init__(self):
        self.balance=0
        self.pin=""
        self.menu()

    
    def menu(self):
        print('''
        select any number from 1 to 4
        press 1 to create pin
        press 2 to for deposite
        press 3 to withdraw moneyy
        press 4 to check balance
        press other key to exit
        
        ''')

    
        user_inut=input("entr any number (1 to 4)")

        if user_inut=="1":
            self.createpin()
        elif user_inut=="2":
            self.deposite()
        elif user_inut=="3":
            self.withdraw()
        elif user_inut=="4":
            self.checkbalance()
        else:
            exit()

    def createpin(self):
        user_pin=input("Enter Pin Number ")
        self.pin=user_pin
        print("Pin Successfully Created!!")
        self.menu()
            


    def deposite(self):
            #for authentication of the useer 
            user_pin=input("Enter Pin Number ")
            if self.pin==user_pin:
                amount=int(input("Enter Your Amount"))
                self.balance = amount+ self.balance
                print("Successfully Credited")
                self.menu()
            else:
                print("Unauthorized Access")
        

    def withdraw(self):
            user_pin=input("Enter Pin Number ")
            if self.pin==user_pin:
                amount =int(input("Enter withdrawel amount")) 
                self.balance= self.balance-amount
                print("Withdraw Successfully")
                self.menu()


    def checkbalance(self):
            user_pin=input("Enter Pin Number ")
            if self.pin==user_pin:
                print("balance:",self.balance)
                self.menu()

sbi=atm()

