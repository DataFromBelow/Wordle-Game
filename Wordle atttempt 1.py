# dependencies
import random
import os


# system variables
# Text colors, i had to look this up
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
RESET = "\033[0m"

while True:
    # clears the terminal, to be made optional
    terminal_clear = input("Clear Terminal? Y/N ").lower()
    if terminal_clear[0] == "y":
        os.system("cls")
    else:
        pass

    # Name of the game, uppercase
    print("WORDLE")
    # Rules of wordle
    print("You get several guesses (currently 6) to guess a word of 5 letters.\n- If you get a letter correct in the right position, it becomes green!\n- If you get a letter correct in the wrong position, it becomes yellow.\n- If you get the letter wrong, it doesn't change colors.")

    # This is where we choose our Word, i got a little help here
    with open("wordle_ord.txt") as f:
        words = f.readlines()
    word_index = int(random.randrange(1, len(words)))
    correct = words[word_index].lower()

    print(f"{correct}")


    # attempts, I would like this to become variable 
    for x in range(6):
        # guess input
        s = 0
        guess = input("State your guess: ").lower()

        # check letters
        for i in range(0, 5):

            if guess[i]==correct[i]:
                print(f"{COLOR_GREEN}{guess[i]}{RESET}", end="")
                s = s+1
            elif guess[i] in correct:
                print(f"{COLOR_YELLOW}{guess[i]}{RESET}", end="")
            else:
                print(guess[i], end="")
        
        print("")

        if s == 5:
            break
    
    
    if s == 5:
        print("╰(°ロ°)╯ We have a winner! You will be sacrificed to the dark gods of chaos!")
        pass


    else:
        print("(┬┬﹏┬┬) We have a loser! Better luck next time! Now you will become a chaos spawn...")
        print(f"This time's word was {correct}")
        pass

    # this should allow replay
    end = input("Would you like to play again and perhaps win? Y/N ").lower()
    if end[0] == "y":
        pass
    else:
        break

# Currently known issues: Out of string crash, If statement not working when it should, some pc's want relative path
