import tkinter as tk
import random
import playsound

# Create a new window
window = tk.Tk()

# Set the dimensions of the created window
window.geometry("800x600+400+100") # widthxheight+x+y
tk.Grid()
# Icons
exit_img = tk.PhotoImage(file='exit.png')
playAgain_img = tk.PhotoImage(file='replay.png')

# Set the background color of the window
window.configure(bg='black')
window.resizable(width=False, height=False)


# Set Window Title
window.title('Bagels')

# The code for the buttons and text and other
# interactive UI elements go here

MAX_GUESSES = 10

# (i) Change the paths
def win():
    playsound.playsound('E:\SEM-1\FOCP\ES_project\Bagels\win.wav')


def wrong():
    playsound.playsound('E:\SEM-1\FOCP\ES_project\Bagels\wrong.wav')


def replay():
    playsound.playsound('E:\SEM-1\FOCP\ES_project\Bagels\\replay.wav')


def getSecretNum():
    """Returns a string made up of 3 unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first 3 digits in the list for the secret number:
    secretNum = ''
    for i in range(3):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        win()
        return 'You got it!\n\nHit 🔄 to start again.'
    else:
        wrong()

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        # There are no correct digits at all.
        return 'Wrong Answer!!\n\nHints: Bagels'
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return 'Wrong Answer!!\n\nHints: '+' '.join(clues)


def update_result(text):
    result.configure(text=text)

# Create a new game


def new_game():

    global numGuesses
    numGuesses = 1
    guess_button.config(state='normal')
    """Returns a string made up of 3 unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.
    global secretNum
    # Get the first 3 digits in the list for the secret number:
    secretNum = ''
    for i in range(3):
        secretNum += str(numbers[i])
    update_result(
        text="I have thought a 3 digit number\n\n\tTry to Guess it!!!\n\nYou have 10 Tries! ")
    replay()
    return secretNum
# Continue the ongoing game or end it


def play_game():

    global secretNum
    global numGuesses

    guess = (number_form.get())

    clues = getClues(guess, secretNum)
    update_result(text=f'Guess # {numGuesses}\n\n{clues}')
    numGuesses += 1

    if numGuesses > MAX_GUESSES:
        update_result(
            text=f'You ran out of guesses.The answer was {secretNum}.\n\n Hit 🔁 to start again.')
        playsound.playsound('E:\SEM-1\FOCP\ES project\Bagels\lose.wav')


Font_family = 'Calibri'
# Heading of our game
title = tk.Label(window, text="🥯 Bagels 🥯", font=(
    Font_family, 50, 'bold'), bg='#964B00')
description = tk.Label(window, text='''\t   Bagels, a deductive logic game.\n
Words\tClues\n
Pico\tOne digit is correct but in the wrong position.
Fermi\tOne digit is correct and in the right position.
Bagels\tNo digit is correct.''', font=(Font_family, 18, "normal", "italic"), bg='black', fg="#b5651d", justify=tk.LEFT)

# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=(
    Font_family, 16, "normal", "italic"), fg="green", bg='black', justify=tk.LEFT)

# Play Button
play_button = tk.Button(window, borderwidth=0, bg='black',
                        image=playAgain_img, command=new_game)
# Guess Button
guess_button = tk.Button(window, borderwidth=0, text="Guess", font=(
    Font_family, 16), state='disabled', fg="white", bg="#964B00", command=play_game)

# Exit Button
exit_button = tk.Button(window, borderwidth=0,
                        image=exit_img, bg='black', command=exit)

# Entry Fields
guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=(Font_family, 16),
                       fg='blue', textvariable=guessed_number)


# Place the labels

title.place(x=180, y=10)
description.place(x=100, y=100)
result.place(x=260, y=390)

# Place the buttons
exit_button.place(x=420, y=530)
guess_button.place(x=350, y=340)
play_button.place(x=270, y=530)

# Place the entry field
number_form.place(x=260, y=305)

# Start the window
window.mainloop()
