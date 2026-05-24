import random

l=["rock","paper","scissors"]
round=1
while round<=5:
    user_input=input("enter rock, paper or scissors: ")
    if user_input not in l:
        print("invalid input")
        continue
    usch=0
    cch=0
    for a in range(5):
        computer_input=random.choice(l)
        print("computer chose: ", computer_input)
    if user_input==computer_input:
        print("it's a tie")
    elif (user_input=="rock" and computer_input=="scissors") or (user_input=="paper" and computer_input=="rock") or (user_input=="scissors" and computer_input=="paper"):
        print("you win")
        usch+=1
    else:
        print("you lose")
        cch+=1
    print("your score: ", usch)
    round+=1