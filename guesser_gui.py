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

# Creating labels
welcome_message = "Welcome to the number guesser!!!"
label_0 = Label(text=welcome_message)
initial_message = "\nThink of a number between 1 and 1000 (including them). I'll take only 10 guesses (or less) to find out which number you picked.\n\nYou'll just have to tell me if your number is smaler or bigger than my guess. Wanna try it?"
label_1 = Label(text=initial_message, wraplength = 450)
message = "\nJust click the buttons telling me when I'm right, or when and still not there, if your number is lower or higher then mine."
label_2 = Label(text=message, wraplength=450)

# Configuring labels
label_0.config(font=("Comic Sans MS",16),fg="#000022",bg="#ccddcc",padx =10, pady=10, width=50)
label_1.config(font=("Verdana",12),)
label_2.config(font=("Verdana",12))

# Displaying labels
label_0.grid(row = 0, column = 0, columnspan =3)
label_1.grid(row = 1, column = 0, columnspan =3)
label_2.grid(row = 2, column = 0, columnspan =3)

# Defining the buttons
but_lower = Button(text="Mine is lower", bg= "#ddccff")
but_right = Button(text="You got me!", bg= "#ddeecc")
but_higher = Button(text="Mine is higher", bg= "#ddccff")

# Displaying the buttons
but_lower.grid(row=3,column=0, pady = 15)
but_right.grid(row=3, column = 1, pady = 15)
but_higher.grid(row=3,column=2, pady = 15 )

# Running main loop
root.mainloop()