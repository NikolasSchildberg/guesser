"""
Welcome to the number guesser in python!
The logic is to use the bissection method to find a number chosen by the user, only
providing guesses and asking to try a bigger or smaller one next time.
"""

# Initial message
print("Welcome to the number guesser!\nThink of a number between 1 and 1000 (including them).I'll take only 10 guesses (or less) to find out which number you picked.\nYou'll just have to tell me if your number is smaler or bigger than my guess. Wanna try it?")
print("Please enter '0' if I'm already right, '1' if your number is smaller, and '2' if your number is bigger.\n")
right = False
smaller = 0
bigger = 1000
guess = int((smaller + bigger)/2)
count_guesses = 0

while(right != True):
    whattodo = input("Is it "+str(guess)+"?\n>>> " )
    if whattodo == '0':
        right = True
    elif whattodo == '1':
        bigger = guess
        guess = int((smaller + bigger)/2)
    elif whattodo == '2':
        smaller = guess
        guess = int((smaller + bigger)/2)
    else: print("Try again...")
    count_guesses += 1
else:
    if(count_guesses == 1):
        print("Gotcha! Needed",count_guesses,"guesse!\nBye!")
    else:
        print("Gotcha! Needed",count_guesses,"guesses!\nBye!")