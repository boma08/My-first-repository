from tkinter import *
import random
import pandas

french_words = {}
current_card = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    french_words = original_data.to_dict(orient="records")
else:
    french_words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_words)
    canvas.itemconfig(translation, text=current_card["French"], fill="black")
    canvas.itemconfig(source_language, text="French", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(source_language, text="English", fill="white")
    canvas.itemconfig(translation, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def known_card():
    french_words.remove(current_card)
    data = pandas.DataFrame(french_words)
    data.to_csv("./data/words_to_learn.csv", index=False) #index set to not include the row index
    next_card()





BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 268, image=card_front_img)
source_language = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
translation = canvas.create_text(400, 263, text=f"{current_card}", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0, padx=50)
known_button = Button(image=right_img, highlightthickness=0, command=known_card)
known_button.grid(row=1, column=1, padx=50)

next_card()

window.mainloop()
