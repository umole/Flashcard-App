BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random


screen = Tk()
screen.config(bg=BACKGROUND_COLOR, highlightthickness=0)
screen.title("Flashy")
screen.config(padx=30, pady=50)
current_card = {}
to_learn = {}

try:
    file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    new_words = pandas.read_csv("./data/french_words.csv")
    to_learn = new_words.to_dict(orient="records")
else:
    to_learn = file.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=front_image)
    flip_timer = screen.after(3000, change_card)


def change_card():
    canvas.itemconfig(canvas_img, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


flip_timer = screen.after(3000, change_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 260, image=front_image)
title_text = canvas.create_text(400, 180, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="")
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.config(padx=50, pady=50)
wrong_button.grid(row=1, column=0, columnspan=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.config(bg=BACKGROUND_COLOR)
right_button.config(padx=50, pady=50)
right_button.grid(row=1, column=1, columnspan=1)

next_card()




screen.mainloop()