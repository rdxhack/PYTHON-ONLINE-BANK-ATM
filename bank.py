print("welcome to the online ATM LAVKUSH VISHWAKARMA")
restart = ('y')
balance = 999.9
chances = 3
while chances>=0:
    pin=int(input("enter your 4 digits pin code your code is 1234 :"))
    if pin == (1234):
        print("you enter corret pin code")
        print("please enter 1 for your balance")
        print("please enter 2 to make withdrawl")
        print("please enter 3 to Pay in:")
        print("please enter 4 to return card")
        while restart not in ('n','N','NO','no'):
            print("please enter 1 for your balance")
            print("please enter 2 to make withdrawl")
            print("please enter 3 to Pay in:")
            print("please enter 4 to return card")

            option=int(input("what would you like to choose:?"))
            if option==1:
                print("yur balance is $",balance)
                restart=input("would you like to go back please enter y")
                if restart in ('n','N','NO','no'):
                    print("thank you using online ATM LAVKUH VISHWAKARMA")
                    break
            elif option ==2:
                 option=('y')
                 withdrawl =float(input("how much you withdrawl ?10,20,30,40,50,60,70,80,90,100 for other enter 1:"))
                 if withdrawl in [10,20,30,40,50,60,70,80,90,100]:
                     balance=balance-withdrawl
                     print("\nyour current balance $:",balance)
                     restart =input("would you like to go back please enter N")
                     if restart in ('n','N','NO','no'):
                         print("thank you using online ATM LAVKUH VISHWAKARMA") 
                         break
                     elif withdrawl !=[10,20,30,40,50,60,70,80,90,100]:
                         print("invalide amount please re-enter\n")
                         restart=('y')
                     elif withdrawl == 1:
                        withdrawl=float(input("please enter perfect amount:"))                                                                   
            elif option==3:
                pay_in=float(input("how much you will pay money of your friends:"))
                balance=balance+pay_in
                print("\nyour balance is NOW$:",balance)
                restart=input("would you like to go back")
                if restart in ('n','N','NO','no'):
                    print("\nthanks you using online ATM LAVKUH VISHWAKARMA")
                    break
            elif option==4:
                print("please wait to return your cards....\n")
                print("thanks for using our service thanks using online ATM LAVKUH VISHWAKARMA ") 
                break           
            else:
                print("please enter the correct pin code \n")
                restart=('y')
    elif pin !=('1234'):
                   print("incorrect password")
                   chances=chances-1                 
    if chances==0:
     print("\n sorry no more tries")
     break              
              































                
                               
