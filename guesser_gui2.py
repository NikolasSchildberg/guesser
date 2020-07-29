"""
Welcome to the number guesser in python!
The logic is to use the bissection method to find a number chosen by the user, only
providing guesses and asking to try a bigger or smaller one next time.
"""

from tkinter import *

# Root screen on tkinter
root = Tk()
root.title("Number Guesser")
#root.geometry("600x400+500+100")

# Implementation of the Algorithm per se
mini = 0
maxi = 1000
guess = int((mini+maxi)/2)
count_guesses = 1

def key(event):
    if repr(event.char) == 'a':
        print("Ha!")
frame = Frame(root, width=100, height=100)
frame.bind("<Left>", lambda: lower_clicked)
frame.bind("<Right>", lambda: higher_clicked)

def higher_clicked():
    global mini, maxi, guess, count_guesses, usermessage
    mini = guess
    guess = int((mini+maxi)/2)
    count_guesses += 1
    usermessage = "My guess:\n"+str(guess)+"\nGuesses so far:"+str(count_guesses)
    label_3_guess.config(text=usermessage)
    #print("guess:",guess,"\nmini:",mini,"\nmaxi:",maxi)

def lower_clicked():
    global mini, maxi, guess, count_guesses, usermessage
    maxi = guess
    guess = int((mini+maxi)/2)
    count_guesses += 1
    usermessage = "My guess:\n"+str(guess)+"\nGuesses so far:"+str(count_guesses)
    label_3_guess.config(text=usermessage)
    #print("guess:",guess,"\nmini:",mini,"\nmaxi:",maxi)
    
def right_clicked():
    global mini, maxi, guess, count_guesses, usermessage
    if(count_guesses == 1):
        usermessage = "Your number:\n"+str(guess)+"\nHa! Gotcha with 1 guess!"
    else:
        usermessage = "Your number:\n"+str(guess)+"\nHa! Gotcha with "+str(count_guesses)+" guesses!"
    label_3_guess.config(text=usermessage)
    but_lower.destroy()
    but_right.destroy()
    but_higher.destroy()
    
# Creating labels
welcome_message = "Welcome to the number guesser!!!"
label_0 = Label(text=welcome_message)
initial_message = "\nThink of a number between 1 and 1000 (including them). I'll take only 10 guesses (or less) to find out which number you picked.\n\nYou'll just have to tell me if your number is smaler or bigger than my guess. Wanna try it?"
label_1 = Label(text=initial_message, wraplength = 400)
message = "\nJust click the buttons telling me when I'm right, or when and still not there, if your number is lower or higher then mine.\n"
label_2 = Label(text=message, wraplength=400)
usermessage = "My guess:\n"+str(guess)+"\nGuesses so far:"+str(count_guesses)
label_3_guess = Label(text=usermessage) #current guess to display

# Configuring labels
label_0.config(font=("Comic Sans MS",15),
               fg="#000022",
               bg="#ddddde",
               padx =50,
               pady=10)
label_1.config(font=("Verdana",12),)
label_2.config(font=("Verdana",12))
label_3_guess.config(font=("Comic Sans MS", 20),
                     bg ="#ffeeff",
                     fg="#000033",
                     borderwidth=2,
                     relief="sunken",
                     padx = 0,
                     pady =0)

# Displaying labels
label_0.grid(row = 0, column = 0, columnspan =3)
label_1.grid(row = 1, column = 0, columnspan =3)
label_2.grid(row = 2, column = 0, columnspan =3)
label_3_guess.grid(row = 3, column = 0, columnspan =3,ipadx=40, ipady=0)

# Defining the buttons
but_lower = Button(text="Mine is lower", bg= "#ddccee", command = lower_clicked)
but_right = Button(text="You got me!", bg= "#ddeecc", command = right_clicked)
but_higher = Button(text="Mine is higher", bg= "#ddccee", command = higher_clicked)
but_quit = Button(text="Quit", command = root.destroy)

# Displaying the buttons
but_lower.grid(row=4,column=0, pady = 15)
but_right.grid(row=4, column = 1, pady = 15)
but_higher.grid(row=4,column=2, pady = 15 )
but_quit.grid(row=5, column=1, pady = 10)

# Running main loop
root.mainloop()