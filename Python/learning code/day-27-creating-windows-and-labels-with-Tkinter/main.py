import tkinter

window = tkinter.Tk()

# include title
window.title("My first GUI program")

# specify minimum size of the window
window.minsize(width=500, height=300)

# add a label and pack it to the center of the screen
my_label = tkinter.Label(text="I am a label", font=("Arial", 12, "italic"))
my_label.pack()

my_label["text"] = "New text update"  # changes the from during initialisation to the new text
# my_label.config(text= "New text", font= ("Courier", 12, "bold"))  # Updates the text and font arguments from line 12


def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=user_input.get())


button = tkinter.Button(text="click me", command=button_clicked)  # the command keyword is like a listener that
# runs each time the button is clicked
button.pack()  # anytime an object to be displayed on screen is created, it has tbe packed using obj.pack()


#  Input into a GUI
user_input = tkinter.Entry(width=10)
user_input.pack()

window.mainloop()





