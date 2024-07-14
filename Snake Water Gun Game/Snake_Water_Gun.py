import random

def check(user,com):
    if(user==com):
        print("Draw !")
    elif(user==0 and com==1):
        print("User Win !")    
    elif(user==1 and com==0):
        print("Computer Win !")    
    elif(user==0 and com==2):
        print("Computer  Win !")    
    elif(user==2 and com==0):
        print("User Win !")
    elif(user==1 and com==2):
        print("user Win!") 
    elif(user==2 and com==1):
        print("com Win !")
   

com =random.randint(0,2)
user =int(input("0 for Snak,1 for Water,2 for Gun:"))
print(f"computer Choice:{com}")
check(user,com)
