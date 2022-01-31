##############################################################
##############        Module Import Area        ##############
##############################################################

import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox
import random

##############################################################
##############          Variables Area          ##############
##############################################################

blank = ''
CATEGORY = 'Animals Fruits English_Words'.split() # Categories Area
SCORE = 0   # Scoring area
HANGMAN_PICS = ['start', 1, 2, 3, 4, 5, 6] # Pics sourse list
missedLetters = []  # List of incorrect letter guesses.
correctLetters = []  # List of correct letter guesses.
secretWor = ''  # Hidden word

##############################################################
##############        GAME Function Area        ##############
##############################################################

def secret(word):
    '''Word selector Function. Accepts a splitted string
    and choose randomly and returns the choosed word.'''
    global secretWor
    secretWor = random.choice(word)
    return secretWor

def drawHangman(missedLetters, correctLetters, secretWord):
    '''Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word.'''
    hangman.configure(file=f"assets/{HANGMAN_PICS[len(missedLetters)]}.png")

    wrong_guess = ''
    # Show the incorrectly guessed letters
    for letter in missedLetters:
        wrong_guess += f'{letter}, '
    wrong_guess_label.configure(text=wrong_guess)

    # Display the blanks for the secret word (one blank per letter)
    blanks = ['_ '] * len(secretWord)

    # Replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]
    global blank
    # Show the secret word with spaces in between each letter
    blank = ' '.join(blanks)
    updateWord(blank)

def getPlayerGuess(alreadyGuessed, guess):
    '''Returns the letter the player entered. This function makes sure
    the player entered a single letter they haven't guessed before.'''
    # Keep asking until the player enters a valid letter.

    if len(guess) != 1:
        msg = 'Enter a single letter'
    elif guess in alreadyGuessed:
        msg = 'You have already guessed that letter. Choose again.'
    elif not guess.isalpha():
        msg = 'Please enter a LETTER.'
        str(guess)
    else:
        return guess
    entry.delete(0,len(guess))
    messagebox.showerror('Invalid input', msg)

def updateWord(blank):
    '''Update the status of word on screen!'''
    word.configure(text=blank)

def newGame():
    '''Reset or new game generator. Reset the game and score.
        Accepts no argument but returns reseted environment'''
    # Reseting variables for a new game:
    global missedLetters, correctLetters, secretWord, WORDS, CATEGORY, HANGMAN_PICS, desc
    missedLetters = [] 
    correctLetters = []
    category = random.choice(CATEGORY) # Randomly choose category
    if category == 'Animals':
        WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()
    elif category == 'Fruits':
        WORDS = 'MANGOES CHIKOO ORANGE PLUMS APPLES GRAPES GUAVA CHERRY PEACH PEAR APRICOT JAMMON LYCHEE PAPAYA POMEGRANATE'.split()
    else:
        WORDS = '''ABILITY ABLE ABOUT ABOVE ACCEPT ACCORDING ACCOUNT ACROSS ACT ACTION ACTIVITY ACTUALLY ADD ADDRESS ADMINISTRATION ADMIT ADULT AFFECT AFTER AGAIN AGAINST AGE AGENCY AGENT AGO AGREE AGREEMENT AHEAD AIR ALL ALLOW ALMOST ALONE ALONG ALREADY ALSO ALTHOUGH ALWAYS AMERICAN AMONG AMOUNT ANALYSIS AND ANIMAL ANOTHER ANSWER ANY ANYONE ANYTHING APPEAR APPLY APPROACH AREA ARGUE ARM AROUND ARRIVE ART ARTICLE ARTIST AS ASK ASSUME AT ATTACK ATTENTION ATTORNEY AUDIENCE AUTHOR AUTHORITY AVAILABLE AVOID AWAY BABY BACK BAD BAG BALL BANK BAR BASE BE BEAT BEAUTIFUL BECAUSE BECOME BED BEFORE BEGIN BEHAVIOR BEHIND BELIEVE BENEFIT BEST BETTER BETWEEN BEYOND BIG BILL BILLION BIT BLACK BLOOD BLUE BOARD BODY BOOK BORN BOTH BOX BOY BREAK BRING BROTHER BUDGET BUILD BUILDING BUSINESS BUT BUY BY CALL CAMERA CAMPAIGN CAN CANCER CANDIDATE CAPITAL CAR CARD CARE CAREER CARRY CASE CATCH CAUSE CELL CENTER CENTRAL CENTURY CERTAIN CERTAINLY CHAIR CHALLENGE CHANCE CHANGE CHARACTER CHARGE CHECK CHILD CHOICE CHOOSE CHURCH CITIZEN CITY CIVIL CLAIM CLASS CLEAR CLEARLY CLOSE COACH COLD COLLECTION COLLEGE COLOR COME COMMERCIAL COMMON COMMUNITY COMPANY COMPARE COMPUTER CONCERN CONDITION CONFERENCE CONGRESS CONSIDER CONSUMER CONTAIN CONTINUE CONTROL COST COULD COUNTRY COUPLE COURSE COURT COVER CREATE CRIME CULTURAL CULTURE CUP CURRENT CUSTOMER CUT DARK DATA DAUGHTER DAY DEAD DEAL DEATH DEBATE DECADE DECIDE DECISION DEEP DEFENSE DEGREE DEMOCRAT DEMOCRATIC DESCRIBE DESIGN DESPITE DETAIL DETERMINE DEVELOP DEVELOPMENT DIE DIFFERENCE DIFFERENT DIFFICULT DINNER DIRECTION DIRECTOR DISCOVER DISCUSS DISCUSSION DISEASE DO DOCTOR DOG DOOR DOWN DRAW DREAM DRIVE DROP DRUG DURING EACH EARLY EAST EASY EAT ECONOMIC ECONOMY EDGE EDUCATION EFFECT EFFORT EIGHT EITHER ELECTION ELSE EMPLOYEE END ENERGY ENJOY ENOUGH ENTER ENTIRE ENVIRONMENT ENVIRONMENTAL ESPECIALLY ESTABLISH EVEN EVENING EVENT EVER EVERY EVERYBODY EVERYONE EVERYTHING EVIDENCE EXACTLY EXAMPLE EXECUTIVE EXIST EXPECT EXPERIENCE EXPERT EXPLAIN EYE FACE FACT FACTOR FAIL FALL FAMILY FAR FAST FATHER FEAR FEDERAL FEEL FEELING FEW FIELD FIGHT FIGURE FILL FILM FINAL FINALLY FINANCIAL FIND FINE FINGER FINISH FIRE FIRM FIRST FISH FIVE FLOOR FLY FOCUS FOLLOW FOOD FOOT FOR FORCE FOREIGN FORGET FORM FORMER FORWARD FOUR FREE FRIEND FROM FRONT FULL FUND FUTURE GAME GARDEN GAS GENERAL GENERATION GET GIRL GIVE GLASS GO GOAL GOOD GOVERNMENT GREAT GREEN GROUND GROUP GROW GROWTH GUESS GUN GUY HAIR HALF HAND HANG HAPPEN HAPPY HARD HAVE HE HEAD HEALTH HEAR HEART HEAT HEAVY HELP HER HERE HERSELF HIGH HIM HIMSELF HIS HISTORY HIT HOLD HOME HOPE HOSPITAL HOT HOTEL HOUR HOUSE HOW HOWEVER HUGE HUMAN HUNDRED HUSBAND I IDEA IDENTIFY IF IMAGE IMAGINE IMPACT IMPORTANT IMPROVE IN INCLUDE INCLUDING INCREASE INDEED INDICATE INDIVIDUAL INDUSTRY INFORMATION INSIDE INSTEAD INSTITUTION INTEREST INTERESTING INTERNATIONAL INTERVIEW INTO INVESTMENT INVOLVE ISSUE IT ITEM ITS ITSELF JOB JOIN JUST KEEP KEY KID KILL KIND KITCHEN KNOW KNOWLEDGE LAND LANGUAGE LARGE LAST LATE LATER LAUGH LAW LAWYER LAY LEAD LEADER LEARN LEAST LEAVE LEFT LEG LEGAL LESS LET LETTER LEVEL LIE LIFE LIGHT LIKE LIKELY LINE LIST LISTEN LITTLE LIVE LOCAL LONG LOOK LOSE LOSS LOT LOVE LOW MACHINE MAGAZINE MAIN MAINTAIN MAJOR MAJORITY MAKE MAN MANAGE MANAGEMENT MANAGER MANY MARKET MARRIAGE MATERIAL MATTER MAY MAYBE ME MEAN MEASURE MEDIA MEDICAL MEET MEETING MEMBER MEMORY MENTION MESSAGE METHOD MIDDLE MIGHT MILITARY MILLION MIND MINUTE MISS MISSION MODEL MODERN MOMENT MONEY MONTH MORE MORNING MOST MOTHER MOUTH MOVE MOVEMENT MOVIE MR MRS MUCH MUSIC MUST MY MYSELF NAME NATION NATIONAL NATURAL NATURE NEAR NEARLY NECESSARY NEED NETWORK NEVER NEW NEWS NEWSPAPER NEXT NICE NIGHT NO NONE NOR NORTH NOT NOTE NOTHING NOTICE NOW N'T NUMBER OCCUR OF OFF OFFER OFFICE OFFICER OFFICIAL OFTEN OH OIL OK OLD ON ONCE ONE ONLY ONTO OPEN OPERATION OPPORTUNITY OPTION OR ORDER ORGANIZATION OTHER OTHERS OUR OUT OUTSIDE OVER OWN OWNER PAGE PAIN PAINTING PAPER PARENT PART PARTICIPANT PARTICULAR PARTICULARLY PARTNER PARTY PASS PAST PATIENT PATTERN PAY PEACE PEOPLE PER PERFORM PERFORMANCE PERHAPS PERIOD PERSON PERSONAL PHONE PHYSICAL PICK PICTURE PIECE PLACE PLAN PLANT PLAY PLAYER PM POINT POLICE POLICY POLITICAL POLITICS POOR POPULAR POPULATION POSITION POSITIVE POSSIBLE POWER PRACTICE PREPARE PRESENT PRESIDENT PRESSURE PRETTY PREVENT PRICE PRIVATE PROBABLY PROBLEM PROCESS PRODUCE PRODUCT PRODUCTION PROFESSIONAL PROFESSOR PROGRAM PROJECT PROPERTY PROTECT PROVE PROVIDE PUBLIC PULL PURPOSE PUSH PUT QUALITY QUESTION QUICKLY QUITE RACE RADIO RAISE RANGE RATE RATHER REACH READ READY REAL REALITY REALIZE REALLY REASON RECEIVE RECENT RECENTLY RECOGNIZE RECORD RED REDUCE REFLECT REGION RELATE RELATIONSHIP RELIGIOUS REMAIN REMEMBER REMOVE REPORT REPRESENT REPUBLICAN REQUIRE RESEARCH RESOURCE RESPOND RESPONSE RESPONSIBILITY REST RESULT RETURN REVEAL RICH RIGHT RISE RISK ROAD ROCK ROLE ROOM RULE RUN SAFE SAME SAVE SAY SCENE SCHOOL SCIENCE SCIENTIST SCORE SEA SEASON SEAT SECOND SECTION SECURITY SEE SEEK SEEM SELL SEND SENIOR SENSE SERIES SERIOUS SERVE SERVICE SET SEVEN SEVERAL SEX SEXUAL SHAKE SHARE SHE SHOOT SHORT SHOT SHOULD SHOULDER SHOW SIDE SIGN SIGNIFICANT SIMILAR SIMPLE SIMPLY SINCE SING SINGLE SISTER SIT SITE SITUATION SIX SIZE SKILL SKIN SMALL SMILE SO SOCIAL SOCIETY SOLDIER SOME SOMEBODY SOMEONE SOMETHING SOMETIMES SON SONG SOON SORT SOUND SOURCE SOUTH SOUTHERN SPACE SPEAK SPECIAL SPECIFIC SPEECH SPEND SPORT SPRING STAFF STAGE STAND STANDARD STAR START STATE STATEMENT STATION STAY STEP STILL STOCK STOP STORE STORY STRATEGY STREET STRONG STRUCTURE STUDENT STUDY STUFF STYLE SUBJECT SUCCESS SUCCESSFUL SUCH SUDDENLY SUFFER SUGGEST SUMMER SUPPORT SURE SURFACE SYSTEM TABLE TAKE TALK TASK TAX TEACH TEACHER TEAM TECHNOLOGY TELEVISION TELL TEN TEND TERM TEST THAN THANK THAT THE THEIR THEM THEMSELVES THEN THEORY THERE THESE THEY THING THINK THIRD THIS THOSE THOUGH THOUGHT THOUSAND THREAT THREE THROUGH THROUGHOUT THROW THUS TIME TO TODAY TOGETHER TONIGHT TOO TOP TOTAL TOUGH TOWARD TOWN TRADE TRADITIONAL TRAINING TRAVEL TREAT TREATMENT TREE TRIAL TRIP TROUBLE TRUE TRUTH TRY TURN TV TWO TYPE UNDER UNDERSTAND UNIT UNTIL UP UPON US USE USUALLY VALUE VARIOUS VERY VICTIM VIEW VIOLENCE VISIT VOICE VOTE WAIT WALK WALL WANT WAR WATCH WATER WAY WE WEAPON WEAR WEEK WEIGHT WELL WEST WESTERN WHAT WHATEVER WHEN WHERE WHETHER WHICH WHILE WHITE WHO WHOLE WHOM WHOSE WHY WIDE WIFE WILL WIN WIND WINDOW WISH WITH WITHIN WITHOUT WOMAN WONDER WORD WORK WORKER WORLD WORRY WOULD WRITE WRITER WRONG YARD YEAH YEAR YES YET YOU YOUNG YOUR YOURSELF'''.split()
    # Update Screen
    desc.configure(
        text=f'A word is generated. Guess a letter!\nThe category is: {category}')
    secretWord = secret(WORDS)  # The word the player must guess.
    drawHangman(missedLetters, correctLetters, secretWord)
    return missedLetters, correctLetters, secretWord

def main():
    '''Controls the main Window and events happening'''
    global missedLetters, correctLetters, secretWord, SCORE
    drawHangman(missedLetters, correctLetters, secretWord)

    # Let the player enter their letter guess:
    guess = getPlayerGuess(missedLetters + correctLetters,
                           guess=entry.get().upper())
    if guess in secretWord:
        # Add the correct guess to correctLetters:
        correctLetters.append(guess)
        guess_result.configure(text='Correct!')
        drawHangman(missedLetters, correctLetters, secretWord)
        # Check if the player has won:
        foundAllLetters = True  # Start off assuming they've won.
        for secretWordLetter in secretWord:
            if secretWordLetter not in correctLetters:
                # There's a letter in the secret word that isn't
                # yet in correctLetters, so the player hasn't won:
                foundAllLetters = False
                break
        if foundAllLetters:
            SCORE += 5
            score.configure(text=f'Your Score: {SCORE}')
            guess_result.configure(
                text=f'You got it ! The secret word was:\n{secretWord}')
            missedLetters, correctLetters, secretWord = newGame()

    else:
        # The player has guessed incorrectly:
        missedLetters.append(guess)
        guess_result.configure(text='Wrong!')
        drawHangman(missedLetters, correctLetters, secretWord)
        # Check if player has guessed too many times and lost. (The
        # "- 1" is because we don't count the empty gallows in
        # HANGMAN_PICS.)
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            window.destroy()
    entry.delete(0, len(guess))
            
##############################################################
##############          Display System          ##############
##############################################################
            
window = tk.Tk() # Initialization
# Properties
window.geometry("800x600+400+100")
window.configure(bg="#FFFFFF")

# Important Canvas

'''Creation'''
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0) # Placement

''' Name Of Game '''
canvas.create_text(
    110.0,
    10.0,
    anchor="nw",
    text="Hangman",
    fill="#E91E63",
    font=("Roboto Black", 50 * -1)
)
canvas.create_text(
    10.0,
    10.0,
    anchor="nw",
    text="The",
    fill="#3F51B5",
    font=("Roboto Black", 50 * -1,)
)

''' Wrong Guess Area '''
wrong_guess = 'Wrong Guesses:\n\n'
canvas.create_text(
    280.0,
    470.0,
    anchor="nw",
    text=wrong_guess,
    fill="#E91E63",
    font=("Roboto Black", 30 * -1)
)

''' Hangman Upgradation Area '''
hangman = PhotoImage(
    file="assets/image_1.png")
image = canvas.create_image(
    120.0,
    300.0,
    image=hangman
)

# Important Labels

''' Score label '''
score = tk.Label(
    text='Your Score: ',
    fg='indigo', bg='white',
    font=("Roboto Black", 30 * -1,)
)
score.place(x=550, y=20)

''' Description Label '''
desc = tk.Label(
    text='Hangman is a word-guessing game. The\nnumber of letters of word is shown by\n dashes and when you guess a letter it\n is filled in appropriate location\n\nHit the 🔁 button to start and reset\nUse the other button on the right\n side to check',
    fg="#3F51B5", bg='white',
    font=("Roboto Black", 30 * -1,)
)
desc.place(x=260.0, y=100.0)

''' Guessed Result Status '''
guess_result = tk.Label(
    text='',
    fg="red", bg='white',
    font=("Roboto Black", 30 * -1,)

)
guess_result.place(x=260.0, y=200.0)

'''Word upgradation'''
word = tk.Label(
    text='',
    fg="orange", bg='white',
    font=("Roboto Black", 50 * -1)
)
word.place(x=300.0, y=305.0)

''' Wrong Guesses Area '''
wrong_guess_label = tk.Label(
    text='No missed letter yet!',
    fg='#3F51B5', bg='white',
    font=("Roboto Black", 30 * -1)
)
wrong_guess_label.place(x=320, y=510)

# Taking input from user
guess_entry = tk.StringVar()
entry = Entry(
    font=("Roboto Black", 40 * -1),
    fg='yellow',
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=guess_entry
)
entry.place( x=430.0, y=400.0, width=50.0, height=50.0)

# Important Buttons

'''Guess and Check button'''
button_image_1 = PhotoImage(
    file="assets/button_1.png")
guess_btn = Button(
    image=button_image_1,
    borderwidth=0,
    bg='white',
    highlightthickness=0,
    command=main,
    relief="flat"
)
guess_btn.place( x=500.0, y=400.0, width=50.0, height=50.0)

''' RESET button or restart Button'''
new_game = PhotoImage(
    file="assets/replay.png")
new_game_btn = Button(
    image=new_game,
    borderwidth=0,
    bg='white',
    highlightthickness=0,
    command=newGame,
    relief="flat"
)
new_game_btn.place( x=350.0, y=395.0, width=60.0, height=60.0)

window.resizable(False, False)

# Main game loop function
window.mainloop()
    
