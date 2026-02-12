import random
import os
from sys import exit
# clears the terminal
os.system("cls")

# Name of the game, uppercase
print("WORDLE")

# This is where we choose our Word, i got a little help here
with open("wordle_ord.txt") as f:
    words = f.readlines()
word_index = int(random.randrange(1, len(words)-1))
correct = words[word_index].lower()

print(f"{correct}")

# Colors, i had to look this up
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
RESET = "\033[0m"

# attempt at Attempts, might become variable 
for x in range(6):
    # guess input
    s = 0
    guess = input("State your guess: ").lower()

    #    if guess == correct:
    #        print("hippo")
    #        break
    #    else:
    #        print("if statement ignored")
    # check letters
    for i in range(0, 5):
        if guess == correct:
            print("╰(°ロ°)╯ We have a winner!")
            exit()
            break
        elif guess[i]==correct[i]:
            print(f"{COLOR_GREEN}{guess[i]}{RESET}", end="")
            s = s+1
        elif guess[i] in correct:
            print(f"{COLOR_YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")
    
    print("")

    if s == 5:
        print("╰(°ロ°)╯ We have a winner!")
        break
    
    if guess == correct:
        print("╰(°ロ°)╯ We have a winner!")
        exit()
    
#    print("╰(°ロ°)╯ We have a winner!")
#    exit()
    else:
        print("(┬┬﹏┬┬) We have a loser! Better luck next time!")
        print(f"This time's word was {correct}")
#    print("(┬┬﹏┬┬) We have a loser! Better luck next time!")
#    print(f"This time's word was {correct}")

# Currently known issues: Out of string crash, If statement not working when it should