import tkinter as tk
import random
# Set up the constants:
# The garbage filler characters for the "computer memory" display.

GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'
# Load the WORDS list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline:
    WORDS[i] = WORDS[i].strip().upper()

def play():
    desc.configure(
    font=('Roboto',20),
    fg='green',bg='black'
)
    desc.place(x=10,y=80)
    askForPlayerGuess()
    tri.configure(text='')
    
def main():
    """Run a single game of Hacking."""
    global gameWords, computerMemory, secretPassword, triesRemaining
    playerMove = guess_entry.get().upper()
    # Start at 4 tries remaining, going down:
    if playerMove in gameWords:
        if playerMove == secretPassword:
            image.configure(file='granted.png')
            correct.configure(text='')
            correct.place(x=600,y=650)
            play()
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            image.configure(file='denied.png')
            correct.configure(text=f'{numMatches}/7 correct')
            correct.place(x=600,y=650)
            triesRemaining -= 1
            triesRemain(triesRemaining)
        
        
    else:
        correct.configure(text='That is not one of the\npossible passwords listed\nabove.',fg='blue')
        correct.place(x=510,y=560)

    if triesRemaining == 0:
        getResult(secretPassword)
    user_guess.delete(0,len(playerMove))

def getResult(secretPassword):

    desc.configure(text=f'Out of tries.\n\nSecret password\n\nwas {secretPassword}.',font=('Terminal',48),fg='red',justify='center')
    desc.place(x=50,y=150)

def getWords():
    """Return a list of 12 words that could possibly be the password.

    The secret password will be the first word in the list.
    To make the game fair, we try to ensure that there are words with
    a range of matching numbers of letters as the secret word."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two more words; these have zero matching letters.
    # We use "< 3" because the secret password is already in words.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # Find two words that have 3 matching letters (but give up at 500
    # tries if not enough can be found).
    for i in range(500):
        if len(words) == 5:
            break  # Found 5 words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).
    for i in range(500):
        if len(words) == 12:
            break  # Found 7 or more words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # Add any random words needed to get 12 words total.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """Returns a random word from WORDS that isn't in blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """Returns the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerMemoryString(words):
    """Return a string representing the "computer memory"."""

    # Pick one line per word to contain a word. There are 16 lines, but
    # they are split into two halves.
    linesWithWords = random.sample(range(16 * 2), len(words))
    # The starting memory address (this is also cosmetic).
    memoryAddress = 16 * random.randint(0, 4000)

    # Create the "computer memory" string.
    computerMemory = []  # Will contain 16 strings, one for each line.
    nextWord = 0  # The index in words of the word to put into a line.
    for lineNum in range(16):  # The "computer memory" has 16 lines.
        # Create a half line of garbage characters:
        leftHalf = ''
        rightHalf = ''
        for j in range(16):  # Each half line has 16 characters.
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)

        # Fill in the password from words:
        if lineNum in linesWithWords:
            # Find a random place in the half line to insert the word:
            insertionIndex = random.randint(0, 9)
            # Insert the word:
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord]
                        + leftHalf[insertionIndex + 7:])
            nextWord += 1  # Update the word to put in the half line.
        if lineNum + 16 in linesWithWords:
            # Find a random place in the half line to insert the word:
            insertionIndex = random.randint(0, 9)
            # Insert the word:
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord]
                         + rightHalf[insertionIndex + 7:])
            nextWord += 1  # Update the word to put in the half line.

        computerMemory.append('0x'+hex(memoryAddress)[2:].zfill(4)
        + '\t' + leftHalf + '\t\t' + '0x'+hex(memoryAddress
        + (16*16))[2:].zfill(4) + '\t' + rightHalf) 

        memoryAddress += 16  # Jump from, say, 0xe680 to 0xe690.

    # Each string in the computerMemory list is joined into one large
    # string to return:
    return '\n'.join(computerMemory)


def askForPlayerGuess():
    """Let the player enter a password guess."""
    global guess, gameWords, computerMemory, secretPassword, triesRemaining
    triesRemaining = 4
    gameWords = getWords()
    # The "computer memory" is just cosmetic, but it looks cool:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    user_guess.place(x=50,y=610,width=130)
    try_btn.place(x=195,y=605,width=49,height=49)
    desc.configure(text=computerMemory, font=('Roboto',18), justify='left')
    
    guess = user_guess.get().upper()
    
    
    

def triesRemain(tries):
    tri.configure(text=f'{tries} tries remaining')

game = tk.Tk()

game.geometry('900x750+400+100')
game.resizable(width=False, height=False)

game.title('Password Hacker')

canvas = tk.Canvas(
    game,
    height=750.0,
    width=900.0,
    bg='black',
)
canvas.place(x=0, y=0)

canvas.create_text(
    450.0, 40.0,
    text='Password Hacker',
    font=('Terminal', 50),
    fill='green'
)

desc = tk.Label(
    text='''Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter 
O and N as their 2nd and 3rd letter.\n
    You will get four guesses.\n
    Hit the button to start!''',
font=('Roboto',20),
fg='green',bg='black'
)
desc.place(x=10,y=80)

image = tk.PhotoImage(file='m.png')
result = canvas.create_image(
    690.0,
    600.0,
    image=image
)
correct = tk.Label(
    text='',
    font=('Roboto',25),
    fg='cyan', bg='black'
)
correct.place(x=600,y=650)

tri = tk.Label(
    text='',
    font=('Roboto',20),
    fg='white', bg='black'
)
tri.place(x=340,y=530)

img = tk.PhotoImage(file='Play.png')
play_img = tk.Button(
    image=img,
    bd=0,
    bg='black',
    command=play,
)
play_img.place(x=420,y=580)

guess_entry = tk.StringVar()
user_guess = tk.Entry(
    font=("Roboto Black", 25),
    fg='yellow',
    bd=0,
    bg="gray",
    textvariable=guess_entry
)

try_img = tk.PhotoImage(file='try.png')
try_btn = tk.Button(
    image = try_img,
    bd=0,
    command=main
)


game.mainloop()
