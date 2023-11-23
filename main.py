import tkinter as tk
import json
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """This will randomly generate a password using the lists below, it will have uppercase letters and symbols,
    I think it will meet all the requirements of the websites"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """This will do the saving of the account, it checks if the fields are empty or not,
    and then it will put the data in, and after the input the fields for the website and password gets deleted,
    for a convenient way of inputting"""

    website = entry_website.get().upper()
    mail = entry_mail.get()
    password = entry_password.get()
    new_data = {website: {
        "email": mail,
        "password": password,

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don`t leave any fields empty!")
    else:
        try:
            # It reads the old data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            # If the file doesn't exist it will be created
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updates the old data with the new data
            data.update(new_data)

            # Saves the updated data into the file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            # After all of that it deletes the data from the entry points
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """This function will try and find the data the user is searching for, based on the website.
    If the data he is looking for isn't there a pop-up message will appear as a warning"""

    website = entry_website.get().upper()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exits")

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Creating and putting in place all the labels

label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1)

label_mail = tk.Label(text="Email/Username:")
label_mail.grid(column=0, row=2)

label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3)

# Creating the entry points

entry_website = tk.Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_mail = tk.Entry(width=35)
entry_mail.grid(column=1, row=2, columnspan=2)
entry_mail.insert(0, "email@gmail.com")

entry_password = tk.Entry(width=21)
entry_password.grid(column=1, row=3)

# Creating the buttons

button_generate = tk.Button(text="Generate Password", highlightthickness=0, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = tk.Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

button_search = tk.Button(text="Search", highlightthickness=0, width=15, command=find_password)
button_search.grid(column=2, row=1)

window.mainloop()
