import random
import math



def Bank():
 UserName= str(input("what is your name? "))#username for future to create account in databaza
 if (len(UserName))<5:
    print("minimum characters is 5")
    UserName= str(input("what is your name? "))

 password = str(input("Enter Your password? "))#password for future to create account in databaza
 if(len(password))<6:
    print("minimum characters is 7")
    password = str(input("Enter Your password? "))

 bank = int(input("How much do you want to invest? "))#investing
 withdraw = int(input("how much do you want to withdraw? "))#gamovitanot fuli
 Send= str(input("Do You want to send money? yes or no ")) #to send money to someone 
 people=["soso","tezela","vaso"] # list for only that people that are in "contacts"
 if Send == "yes":
    tosend= str(input("Who Do you want to send? "))#who i want to send in people that i have in contact i can only send money 
    if people[0] == tosend: 
       print("You Choosed "+tosend)
    if people[1] == tosend: 
       print("You Choosed "+tosend)
    if people[2] == tosend: 
       print("You Choosed "+tosend)
    else:
     print("there is no " + tosend)
    if True:
       howmany= int(input("how much do you want to send? "))
       print(UserName+" Your Balance is: "+str(bank-withdraw-howmany))
       print(tosend+" has "+ str(int(random.randint(1,1000)) + int(howmany)))

 if Send == "no":
    print("Ok")


 if bank > withdraw:
     print(UserName+" Your Balance is: "+str(bank-withdraw))
 elif bank == withdraw:
     print(UserName+"Yout Balance is: "+str(bank-withdraw))
 else:
     print("You dont have enough money")
Bank()

