import random
from datetime import time

operator=""
AIoperator=""
win="You Win :)"
lose="AI Wins :("
draw="Its a Draw :/"
result=""
error="Unable to determine winner - Error"
rock="Rock"
paper="Paper"
scissors="Scissors"
again=True


def printspace(lines):
    linescount=range(lines)
    for line in linescount:
        print("")


def Random():
    ranint=random.randint(1, 3)
    return ranint

    
def random_operator():
    num=Random()
    if num == 1:
        AIoperator="Rock"
        return AIoperator
    elif num == 2:
        AIoperator="Paper"
        return AIoperator
    else:
        AIoperator="Scissors"
        return AIoperator


def determine_winner(Player, Ai):
    if Player==Ai:
        result=draw
    
    elif Player!=Ai:
        if Player=="Rock" and Ai=="Paper":
            result=lose
        elif Player=="Rock" and Ai=="Scissors":
            result=win

        elif Player=="Paper" and Ai=="Rock":
            result=win
        elif Player=="Paper" and Ai=="Scissors":
            result=lose

        elif Player=="Scissors" and Ai=="Rock":
            result=lose
        elif Player=="Scissors" and Ai=="Paper":
            result=win
        
        else:
            result=error
    
    else:
        result=error
    
    return result
            

entergame=False


printspace(15)

print("Welcome to Rock, Paper, Scissors!")

printspace(1)


while entergame==False:
    entergame=input("Press Enter to continue...")

printspace(3)

def game():
    again=False
    operator_input=input("Rock, Paper or Scissors: ")
    printspace(1)

    operator=""

    while operator != "Rock" or operator != "Paper" or operator != "Scissors":
        if operator_input=="Rock" or operator_input=="rock" or operator_input=="ROCK":
            operator="Rock"
            break
        elif operator_input=="Paper" or operator_input=="paper" or operator_input=="PAPER":
            operator="Paper"
            break
        elif operator_input=="Scissors" or operator_input=="scissors" or operator_input=="SCISSORS":
            operator="Scissors"
            break
        else:
            operator_input=input("Invalid, Rock, Paper or Scissors: ")
            printspace(1)
    


    


    printspace(2)
    print("You have chosen: ", operator)
    printspace(1)
    print("The AI has chosen: ", random_operator())
    printspace(2)

    playagain=input("Play Again? Y/N: ")

    if playagain=="Y" or playagain== "y":
        again=True

    else:
        again=False
   

printspace(5)

while again==True:
    print (game())
    printspace(2)


printspace(5)
print("Thanks for playing!!")
printspace(3)





    

            

        

   













