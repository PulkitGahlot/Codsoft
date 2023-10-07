import random as random

choices=('Rock','Paper','Scissors')


playAgainChoice='y'

while(playAgainChoice=='y'):
    userChoice=input("Make a move:\nRock\nPaper\nScissor\n")
    lowerUserChoice=userChoice.lower()
    computerChoice=random.choice(choices)

    if computerChoice=='Rock' and lowerUserChoice=='rock':
        print(f"Computer Choose: {computerChoice}")
        print("Dang! Its a draw.")

    elif computerChoice=='Rock' and lowerUserChoice=='paper':
        print(f"Computer Choose: {computerChoice}")
        print("Congratulations You Win !!")

    elif computerChoice=='Rock' and (lowerUserChoice=='scissor' or lowerUserChoice=='scissors'):
        print(f"Computer Choose: {computerChoice}")
        print("Better Luck next time. You Lost")

    elif computerChoice=='Paper' and lowerUserChoice=='rock' :
        print(f"Computer Choose: {computerChoice}")
        print("Better luck next time. You Lost")

    elif computerChoice=='Paper' and lowerUserChoice=='paper':
        print(f"Computer Choose: {computerChoice}")
        print("Dang! Its a Draw.")

    elif computerChoice=='Paper' and (lowerUserChoice=='scissor' or lowerUserChoice=='scissors'):
        print(f"Computer Choose: {computerChoice}")
        print("Congratulations You win !!")

    elif computerChoice=='Scissors' and lowerUserChoice=='rock':
        print(f"Computer Choose: {computerChoice}")
        print("Congratulations You win !!")

    elif computerChoice=='Scissors' and lowerUserChoice=='paper':
        print(f"Computer Choose: {computerChoice}")
        print("Better luck next time. You Lost")

    elif computerChoice=='Scissors' and (lowerUserChoice=='scissor' or lowerUserChoice=='scissors'):
        print(f"Computer Choose: {computerChoice}")
        print("Dang! Its a Draw")

    else:
        print("You picked wrong. Enter correct Choice.")

    playAgainChoice='n'
    del(computerChoice)
    playAgainChoice=input("Play Again ? [y/n]")

print("See you later, bye!!")