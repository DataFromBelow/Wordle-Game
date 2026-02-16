# dependencies
import random
import os
# system variables
# Text colors, i had to look this up
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
RESET = "\033[0m"
collapse = 0
while True:
    # clears the terminal, to be made optional
    guess_attempts = 6
    word_length = 5
    terminal_clear = input("Clear Terminal? Y/N ").lower()
    if terminal_clear[0] == "y":
        os.system("cls")
    else:
        pass
    # Name of the game, uppercase
    print("WORDLE Knockoff! (play the real thing!)")
    print("\n\nRules of wordle\n\n")
    print(f"You get several guesses (currently 6) to guess a word of 5 letters.\n- If you get a letter correct in the right position, it becomes {COLOR_GREEN}green{RESET}!\n- If you get a letter correct in the wrong position, it becomes {COLOR_YELLOW}yellow{RESET}.\n- If you get the letter wrong, it doesn't change colors.")
    # This is where we choose our Word, i got a little help here
    # I am not hard coding several hundred lines of words when i can make the options variable anyways for later expansion 
    with open("wordle_ord.txt") as f:
        words = f.readlines()
    word_index = int(random.randrange(1, len(words)))
    correct = words[word_index].lower()
    print(f"\n{correct}\n")
    # attempts, I would like this to become variable 
    for x in range(guess_attempts):
        # guess input
        s = 0
        while True:
            guess = input("State your guess: ").lower()
            if len(guess) < word_length:
                print(f"{COLOR_RED}Word must be at least {word_length} letters!{RESET}")
                pass
            else:
                break
        # check letters
        for i in range(0, word_length):

            if guess[i]==correct[i]:
                print(f"{COLOR_GREEN}{guess[i]}{RESET}", end="")
                s = s+1
            elif guess[i] in correct:
                print(f"{COLOR_YELLOW}{guess[i]}{RESET}", end="")
            else:
                print(guess[i], end="")
        print("\n")
        if s == 5:
            break
    if s == 5:
        print("╰(°ロ°)╯ We have a winner! You will be sacrificed to the dark gods of chaos!")
        print("")
        print("The dark gods can have a live sacrifice as a treat!")
        pass
    else:
        print("(┬┬﹏┬┬) We have a loser! Better luck next time! Now you will become a chaos spawn...")
        print(f"This time's word was ", end="")
        print(f"{(correct).upper()}", end="")
        print("!")
        pass
    # this should allow replay
    # Chupoclops was here
    while True:
        end = input("Would you like to play again and perhaps win? Y/N ").lower()
        if end[0] == "y":
            break
        elif end[0] == "n":
            collapse = 1
            break
        else:
            print("\nI do not understand.\n")
            pass
    if collapse == 1:
        break

# Currently known issues: Out of string crash, If statement not working when it should, some pc's want relative path
