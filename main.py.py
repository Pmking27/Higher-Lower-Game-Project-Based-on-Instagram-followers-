# Higher or Lower game base on instagram followers.
import random
from replit import clear
from art import logo,vs
from game_data import data

should_continue=True
score=0

def check_score(account_1,account_2):
    global score
    if (account_1['follower_count']>account_2['follower_count']):
        score+=1
        clear()
        print(logo)
        print(f"You're right!,Current score : {score}")
    else:
        clear()
        print(logo)
        print(f"Sorry ,that's wrong .Final score :{score}") 
        global should_continue
        should_continue=False

print(logo)
account_b=random.choice(data)
while should_continue:
    account_a=account_b
    print(f"compare A : {account_a['name']},{account_a['description']},{account_a['country']}")
    print(vs)
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Against B : {account_b['name']},{account_b['description']},{account_b['country']}")

    users_choice=input("Who has more followers? Type 'A' or 'B' :").lower() 

    if users_choice=='a':
        check_score(account_a,account_b)  
    elif users_choice=='b':
        check_score(account_b,account_a)   
    else:
        print("Invalid choice.")
        should_continue=False         
