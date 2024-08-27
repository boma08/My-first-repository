from tkinter import *
from turtle import Screen


def button_clicked():
    answer = convert_miles_to_km(float(miles_input.get()))
    answer_label.config(text=f"{answer}")


def convert_miles_to_km(miles):
    km = round(miles * 1.60934, 2)
    return km


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.focus()
miles_input.grid(column=1, row=0)

mile_label = Label(text="Miles",font=("Arial", 12))
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to:", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

answer_label = Label(text="0", font=("Arial", 12))
answer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
