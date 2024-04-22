#------------------------------------------IMPORT MODULES--------------------------------------------------------------#
import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
#------------------------------------------PASSWORD GENERATOR----------------------------------------------------------#
def generate_password():
    password_entry.delete(0,END)
    # Create a list of available letters, numbers and symbols
    letters = list(string.ascii_lowercase)
    upper_case_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list('!$%&()*+')


    # Choose the characters to be included in the password
    password_list = []
    while len(password_list) < 16:
        password_list.append(random.choice(letters))
        password_list.append(random.choice(numbers))
        password_list.append(random.choice(symbols))
        password_list.append(random.choice(upper_case_letters))

    # Scramble the characters selected and concatenate them into a string of 16 digits
    random.shuffle(password_list)
    password = ''.join(password_list[:16:])
    password_entry.insert(END,string=password)
    pyperclip.copy(password)
    password_button.config(text="Password Copied")

#---------------------------------------------SAVE PASSWORD------------------------------------------------------------#
def save_password():
    new_website = (website_entry.get()).title()
    new_username = email_entry.get()
    new_password = password_entry.get()

    if new_password == "" or new_username == "" or new_website == "":
        messagebox.showinfo(title="Error",message="Please dont leave any fields empty!")
    else:
        confirm = messagebox.askokcancel(title=new_website,message=f"The following will be added for {new_website}:\nUsername: {new_username}\nPassword: {new_password}")
        if confirm:
            new_data = {new_website: {"Email":new_username,"Password": new_password}}

        #----------------------R/W to JSON file with error handling-----------------------#
            try:
                with open("passwords.json", "r") as file:
                     data = json.load(file)
                     data.update(new_data)
            except JSONDecodeError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
        #------------------------reset fields to defaults---------------------------------#
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                email_entry.insert(END,string="elijaclarke@gmail.com")
                password_entry.delete(0,END)
                messagebox.showinfo(title="Success",message="Details added successfully.")
                password_button.config(text="Generate Password")

#------------------------------------------SEARCH FUNCTION-------------------------------------------------------------#
def search():
    find_website = (website_entry.get()).title()
    website_exits = False
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            for key in data:
                if key == find_website:
                    messagebox.showinfo(title=f"Data for {find_website}",message=f"Username: {data[key]['Email']}\nPassword: {data[key]['Password']}")
                    website_exits = True
                    email_entry.delete(0, END)
                    email_entry.insert(END,string=data[key]['Email'])
                    password_entry.insert(END,string=data[key]['Password'])
                    pyperclip.copy(password_entry.get())
                    password_button.config(text="Password Copied")
    except FileNotFoundError:
        messagebox.showinfo(title=f"No data for {find_website}",message="No entries have been made yet!")
    except JSONDecodeError:
        messagebox.showinfo(title=f"No data for {find_website}",message="No entries have been made yet!")
    else:
        if find_website == "":
            messagebox.showinfo(title="Oops",message="Please enter a website name.")

        elif website_exits == False:
            messagebox.showinfo(title=f"No data for {find_website}",message="There is no entry for this website yet!")


#----------------------------------------------UI SETUP----------------------------------------------------------------#
window = Tk()
window.title("Password Manager")
window.minsize(400,360)
window.config(padx=20,pady=20)

canvas = Canvas(width=160,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,95,image=logo)
canvas.grid(column=1,row=0)

#----------------------------------------------LABELS------------------------------------------------------------------#
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#----------------------------------------------ENTRIES-----------------------------------------------------------------#
website_entry = Entry(width=26)
website_entry.grid(column=1, row=1)

email_entry = Entry(width=45)
email_entry.insert(END,string="elijaclarke@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=26)
password_entry.grid(column=1,row=3)

#-------------------------------------------BUTTONS--------------------------------------------------------------------#
password_button = Button(text="Generate Password",command=generate_password,width=14)
password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=38,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",command=search,width=14)
search_button.grid(column=2,row=1)

window.mainloop() #keep screen open