from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

pass_words = []
to_learn_words = []

#------------------------------ FUNCTION --------------------------------

def next_card():
    global current_word
    global flip_timer
    window.after_cancel(flip_timer)
    # change img
    card.itemconfig(card_img, image=card_front)
    card.itemconfig(title, text=fr_title)

    current_word = random.choice(words)
    card.itemconfig(word_on_card, text=current_word['French'])
    flip_timer = window.after(3000, flip_card)


def is_known():
    words.remove(current_word)
    # print(len(words))

    data = pd.DataFrame(words)
    data.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    global current_word
    # change img
    card.itemconfig(card_img, image=card_back)

    # change text
    en_title = "English"
    en_word = current_word['English']
    card.itemconfig(title, text=en_title)
    card.itemconfig(word_on_card, text=en_word)


#------------------------------ READ DATA--------------------------------

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    words = pd.DataFrame(original_data).to_dict(orient="records")
else:
    words = pd.DataFrame(data).to_dict(orient="records")

# Get a random french word
# print(random.choice(words)['French'])



#--------------------------------- UI -----------------------------------

window = Tk()

window.title("Flashy")
window.config(width=800, height=526, bg=BACKGROUND_COLOR, padx="50px", pady="50px")

flip_timer = window.after(3000, flip_card)


# Card
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.gif")
card_back = PhotoImage(file="./images/card_back.gif")
card_img = card.create_image(400, 263, image=card_front)
card.grid(column=0, row=0, columnspan=2)

# text
fr_title = "French"
title = card.create_text(400, 150, text=fr_title, font=("Arial", 40, "italic"))


# fr_word = "trouve"
current_word = random.choice(words)
fr_word = current_word['French']
word_on_card = card.create_text(400, 263, text=fr_word, font=("Arial", 60, "bold"))




# BUTTONS
# WRONG
wrong = PhotoImage(file="./images/wrong.gif")
wrong_btn = Button(command=next_card,
                   image=wrong,
                   highlightbackground=BACKGROUND_COLOR,
                   highlightcolor=BACKGROUND_COLOR,
                   borderwidth=0)
wrong_btn.grid(column=0, row=1)
# RIGHT
right = PhotoImage(file="./images/right.gif")
right_btn = Button(command=is_known,
                   image=right,
                   highlightthickness=0,
                   highlightbackground=BACKGROUND_COLOR,
                   highlightcolor=BACKGROUND_COLOR,
                   borderwidth=0)
right_btn.grid(column=1, row=1)



window.mainloop()