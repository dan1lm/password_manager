from tkinter import * 
import time
import random
from tkinter import messagebox


window = Tk()
window.title("Password Manager")
window.config(padx = 30, pady = 30)
canvas = Canvas(height = 200, width =200)
img = PhotoImage(file = "password.png")
canvas.create_image(100, 100, image = img)
canvas.grid(row = 0, column = 0, columnspan=3)


def save():
    website = websiteEntry.get()
    password = passwordEntry.get()
    email = emailEntry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(message = 'Please don\'t leave empty fields!')
    else:
        confirmation = messagebox.askokcancel(message = f'Entered details\n___________\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}\n\nProceed?')
        if confirmation:
            with open("data.txt", 'a') as datafile:
                datafile.write('{} | {} | {} \n'.format(website, password, email))
            
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)
            emailEntry.delete(0, END)


def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random_password = ''
    for i in range(10):
        x = random.randint(1,3)
        if x == 1:
            random_password += random.choice(letters)
        elif x == 2:
            random_password += random.choice(numbers)
        else:
            random_password += random.choice(symbols)
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, random_password)


websiteLabel = Label(text = 'website')
websiteLabel.grid(row = 1, column = 0)

emailLabel = Label(text = 'Email')
emailLabel.grid(row = 2, column = 0)

passwordLabel = Label(text = 'password')
passwordLabel.grid(row = 3, column = 0)

websiteEntry = Entry(width = 35)
websiteEntry.grid(row =1, column = 1, columnspan= 2)
websiteEntry.focus()

emailEntry = Entry(width = 35)
emailEntry.grid(row = 2, column = 1, columnspan=2)
emailEntry.insert(0, 'example@gmail.com')

passwordEntry = Entry(width = 21)
passwordEntry.grid(row = 3, column = 1)

generate_password_button = Button(text = "Generate Password", width = 10, command = generatePassword)
generate_password_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 40, command = save)
add_button.grid(row = 4, column = 0, columnspan= 3)


window.mainloop()