from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    import pyperclip

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)  # replaces the two lines of code below
    # for char in password_list:
    #     password += char
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    password_data = password_entry.get()
    username_data = username_entry.get()

    if len(website_data) == 0 or len(password_data) == 0 or len(username_data) == 0:
        messagebox.showinfo(title="Error!", message="Empty field detected, please ensure all fields are filled...")
    else:
        is_ok = messagebox.askyesno(title=website_data, message=f"Are the details correct: \nWebsite: {website_data}\n"
                                                                f"Username: {username_data}\nPassword: {password_data}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_data} | {username_data} | {password_data}\n")

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            username_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, sticky=W, pady=5, padx=5)
username_label = Label(text="Email/Username:", bg="white")
username_label.grid(row=2, column=0, sticky=W, pady=5, padx=5)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky=W, pady=5, padx=5)

website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky=W, pady=5, padx=5)
username_entry = Entry(width=51)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W, pady=5, padx=5)
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky=W, pady=5, padx=5)

gen_password_button = Button(text="Generate Password", bg="white", width=14, command=generate_password)
gen_password_button.grid(row=3, column=2, sticky=W, pady=5, padx=5)
add_button = Button(text="Add", width=43, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W, pady=5, padx=5)

window.mainloop()