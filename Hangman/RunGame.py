from tkinter import Tk,Canvas, Entry, Text, Button, PhotoImage, messagebox
from gui import SCORE,  secretWor
import os

def run():
    gameover.destroy() 
    os.system('RunGame.py')

gameover = Tk()

gameover.geometry("800x600+400+100")
gameover.configure(bg="#FFFFFF")

GOcanvas = Canvas(
    gameover,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

GOcanvas.place(x=0, y=0)
GOcanvas.create_text(
    220.0,
    4.0,
    anchor="nw",
    text="Game Over",
    fill="#3F51B5",
    font=("Roboto Black", 70 * -1, 'bold')
)

image_image_1 = PhotoImage(
    file='assets/image_1.png')
image_1 = GOcanvas.create_image(
    420.0,
    270.0,
    image=image_image_1
)

new_game = PhotoImage(
    file = 'assets\\replay.png'
)
button_1 = Button(
    image=new_game,
    borderwidth=0,
    bg='white',
    highlightthickness=0,
    command=run,
    relief="flat"
)
button_1.place(
    x=350.0,
    y=530.0,
    width=60.0,
    height=60.0
)

# guess_result.configure(
            #     text=f'You have run out of guesses! The word\nwas {secretWord}')
GOcanvas.create_text(
    550.0,
    250.0,
    anchor="nw",
    text=f'{secretWor}',
    fill="orange",
    font=("Roboto Black", 40 * -1)
)
GOcanvas.create_text(
    10.0,
    250.0,
    anchor="nw",
    text=f'You have run out of\nguesses! The word\nwas',
    fill="#E91E63",
    font=("Roboto Black", 30 * -1)
)

GOcanvas.create_text(
    220.0,
    450.0,
    anchor="nw",
    text="Your Score:",
    fill="#E91E63",
    font=("Roboto Black", 50 * -1)
)

GOcanvas.create_text(
    510.0,
    450.0,
    anchor="nw",
    text=SCORE,
    fill="orange",
    font=("Roboto Black", 50 * -1)
)
gameover.resizable(False, False)
gameover.mainloop()

