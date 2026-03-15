from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
# Citirea datelor din fișierul CSV
data1 = pd.read_csv("/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/data/romanian_words.csv")
to_learn = data1.to_dict(orient="records")


current_card = {}

#--------------------MECHANISM----------------#

def change_text():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="Română" , fill = "black")
    canvas.itemconfig(words_text, text=current_card["Romana"] , fill = "black")
    canvas.itemconfig(flash_card , image = card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title_text, text = "English" , fill = "black")
    canvas.itemconfig(words_text, text=current_card["English"] , fill = "black")
    canvas.itemconfig(flash_card , image = card_back)

def is_known():
    global to_learn
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        try:
            data_lvl2 = pd.read_csv("/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/data/romanian_words_lvl2.csv")
            to_learn = data_lvl2.to_dict(orient="records")
            canvas.itemconfig(level_text , text = "Nivelul 2" , fill = "black")
            change_text()
        except FileNotFoundError:
            try:
                data_lvl3 = pd.read_csv("/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/data/romanian_words_lvl3.csv")
                to_learn = data_lvl3.to_dict(orient="records")
                canvas.itemconfig(level_text , text = "Nivelul 3" , fill = "black")
                change_text()
            except FileNotFoundError:
                messagebox.showinfo(title="Felicitări!", message="Ai învățat toate cuvintele!")
                window.destroy()
    else:
        words_to_learn = pd.DataFrame(to_learn)
        words_to_learn.to_csv("/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/words_to_learn.csv", index=False)
        change_text()
#---------------UI INTERFACE------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50 , bg=BACKGROUND_COLOR)
window.title("Grammar Learning APP")
flip_timer = window.after(3000, flip_card)

card_front = PhotoImage(file="/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/images/card_front.png")
card_back = PhotoImage(file="/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/images/card_back.png")
canvas = Canvas(width = 800, height = 526 , bg=BACKGROUND_COLOR , highlightthickness = 0)
flash_card = canvas.create_image(400 , 268 , image = card_front)
title_text = canvas.create_text(400 , 150 , text="Title" , font=("Ariel", 40 , "italic"))
words_text = canvas.create_text(400 , 263 , text="Word" , font=("Ariel", 60 , "bold"))
level_text = canvas.create_text(400, 470 , text = f"Nivelul 1 ", font=("Ariel", 20 , "bold"))
canvas.grid(row = 0 , column = 0 , columnspan=2)


#Butoane
yes_image = PhotoImage(file="/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/images/right.png")
yes_button = Button(image=yes_image , highlightthickness = 0 , command=is_known)
yes_button.grid(row = 1 , column = 1)

no_image = PhotoImage(file="/Users/01mih/OneDrive/Desktop/PYTHON/Words learning app/images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0 , command=change_text)
no_button.grid(row = 1 , column = 0)

change_text()

 
window.mainloop()


