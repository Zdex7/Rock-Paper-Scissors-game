import random

Rock = 0
Paper = 1
Scissor = 2

choice = (input("Enter Rock [0] / Paper [1] / Scissor [2] \n 0/1/2:"))
comp = random.randint(0,2)

if not choice.isdigit():
    input("Please enter a valid digit between 0-2 \n 0/1/2: ")
else:
    choice = int(choice)
    if choice == 0:
        choice = Rock 
    elif choice == 1:
        choice = Paper 
    else:
        choice = Scissor

    if choice == Rock:
        print("You choose Rock!")
    elif choice == Paper:
        print("You choose Paper!")
    else:
        print("You choose Scissors!")

    if comp == 0 or comp == 1 or comp ==2:
        if comp == 0 :
            comp = Rock 
        elif comp == 1 :
            comp = Paper
        else :
            comp = Scissor
    else:
        comp = int(comp)
    if comp == Rock:
        print("Computer chooses Rock!")
        if choice == Rock:
            print("Its a tie!")
        elif choice == Paper:
            print("You win!")
        else:
            print("You lose!")
    else: 
        comp = int(comp)


    if comp == Paper:
        print("Computer chooses Paper!")
        if choice == Rock:
            print("You lose!")
        elif choice == Paper:
            print("Its a tie!")
        else:
            print("You win!")
    else: 
        comp = int(comp)


    if comp == Scissor:
        print("Computer chooses Scissors!")
        if choice == Rock:
            print("You win!")
        elif choice == Paper:
            print("You lose!")
        else:
            print("Its a tie!")
    else: 
        comp = int(comp)