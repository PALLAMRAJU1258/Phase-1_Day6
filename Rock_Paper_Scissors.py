"""
Write a program to create a rock-paper-scissors
"""

import random as r
n=int(input("No of Matches to play:"))
arr=["rock","paper","scissors"]
comp_score=user_score=0
for i in range(n):
    c_choice=arr[r.randint(0,2)]
    u_choice=input("Enter your choice:").lower()
    if u_choice not in arr:
        print("Invalid choice")
    else:
        if c_choice == "rock" and  u_choice == "paper" :
            print("user won")
            user_score+=1
        elif c_choice == "paper" and u_choice == "scissors" :
            print("user won")
            user_score+=1
        elif c_choice == "scissors" and u_choice == "rock" :
            print("user won")
            user_score+=1
        elif c_choice == u_choice :
            print("Match Draw")
        else:
            print("computer won")
            comp_score+=1
        print(f"computer:{comp_score}\nuser:{user_score}")
if comp_score > user_score :
    print("Computer wins the Game")
elif comp_score == user_score :
    print("the Game is draw(Both computer and user have same point)")
else:
    print("User wins the Game")

#Another method by using recursive function
"""
import random as r
def Rock_Paper_Scissors(arr,n,comp_score,user_score,count):
    c_choice=arr[r.randint(0,2)]
    u_choice=input("Enter your choice:").lower()
    if u_choice not in arr:
        print("Invalid choice")
    else:
        if c_choice == "rock" and  u_choice == "paper" :
            print("user won")
            user_score+=1
        elif c_choice == "paper" and u_choice == "scissors" :
            print("user won")
            user_score+=1
        elif c_choice == "scissors" and u_choice == "rock" :
            print("user won")
            user_score+=1
        elif c_choice == u_choice :
            print("Match Draw")
        else:
            print("computer won")
            comp_score+=1
        print(f"computer:{comp_score}\nuser:{user_score}")
    count+=1
    if count == n:
        if comp_score > user_score :
            print("Computer wins the Game")
        elif comp_score == user_score :
            print("the Game is draw(Both computer and user have same point)")
        else:
            print("User wins the Game")
    else:
        Rock_Paper_Scissors(arr,n,comp_score,user_score,count)
    

n=int(input("No of matches to be played:"))
Rock_Paper_Scissors(["rock","paper","scissors"],n,0,0,0)
"""

#Another method by using choice() from random 
"""
import random as r
n=int(input("No of Matches to play:"))
list_choice=["rock","paper","scissors"]
comp_score=user_score=0
for i in range(n):
    c_choice=r.choice(list_choice)
    u_choice=input("Enter your choice:").lower()
    
    if u_choice not in list_choice:
        print("Invalid choice")
    else:
        if c_choice == "rock" and  u_choice == "paper" :
            print("user won")
            user_score+=1
        elif c_choice == "paper" and u_choice == "scissors" :
            print("user won")
            user_score+=1
        elif c_choice == "scissors" and u_choice == "rock" :
            print("user won")
            user_score+=1
        elif c_choice == u_choice :
            print("Match Draw")
        else:
            print("computer won")
            comp_score+=1
        print(f"computer:{comp_score}\nuser:{user_score}")
if comp_score > user_score :
    print("Computer wins the Game")
elif comp_score == user_score :
    print("the Game is draw(Both computer and user have same point)")
else:
    print("User wins the Game")
"""






        






