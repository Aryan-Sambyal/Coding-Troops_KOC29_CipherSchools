print("Welcome To the game")
print(
    """DESCRIPTION of the game - This a game where you enter a choice i.e. rock, paper, scissors.
Then the computer will also make a choice""")
print("Press p for playing")
x = "p"
z = str(input("Wanna play:"))
user_scored = 0
comp_scored = 0
while z == x:
    a = ["rock", "paper", "scissors"]
    b1 = str(input("Enter your choice: "))
    user_pick = b1.lower()
    import random
    comp_pick = random.choice(a)
    if user_pick == "rock" or user_pick == "paper" or user_pick == "scissors":
        print("your choice =", b1)
        print("computer choice =", comp_pick .lower())
    else:
        print(" invalid: choose any one -- rock, paper, scissors ")
        comp_score = 0
        user_score = 0
    if user_pick == comp_pick:
        print( "Tie,you both select same" )
        comp_score = 0
        user_score = 0
    elif user_pick == 'rock' and comp_pick == 'paper':
        comp_score = 1
        user_score = 0
        print( "You loose,computer select paper \033")
    elif user_pick == 'rock' and comp_pick == 'scissors':
        user_score = 1
        comp_score = 0
        print("You win,computer select scissors")
    elif user_pick == 'paper' and comp_pick == 'scissors':
        comp_score = 1
        user_score = 0
        print("You loose,computer select scissors")
    elif user_pick == 'paper' and comp_pick == 'rock':
        user_score = 1
        comp_score = 0
        print( "You win,computer select rock")
    elif user_pick == 'scissors' and comp_pick == 'rock':
        comp_score = 1
        user_score = 0
        print("You loose,computer select rock")
    elif user_pick == 'scissors' and comp_pick == 'paper':
        user_score = 1
        comp_score = 0
        print("You win ,computer select paper")
    user_scored = user_scored + user_score
    comp_scored = comp_scored + comp_score
    results = "Your score:" + str(user_scored) + ",Computer score:" + str(comp_scored)
    print(results)