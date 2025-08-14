#!/usr/bin/env python3
from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get() == '' and passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fiels are required')
    elif usernameEntry.get()=='admin' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success', 'Login is successful')
        with open('current_role.txt', 'w') as f:
            f.write('admin')
        root.destroy()
        import ems
    elif usernameEntry.get()=='po' and passwordEntry.get()=='1111':
        messagebox.showinfo('Success', 'Login is successful')
        with open('current_role.txt', 'w') as f:
            f.write('po')
        root.destroy()
        import ems
    elif usernameEntry.get()=='clerk' and passwordEntry.get()=='0000':
        messagebox.showinfo('Success', 'Login is successful')
        with open('current_role.txt', 'w') as f:
            f.write('clerk')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'wrong credentials')

root = CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')

bg_image = CTkImage(Image.open('login.jpg'), size=(478,478)) 
label = CTkLabel(root, image=bg_image, text="")
label.place(x=465, y=0)

headingLabel = CTkLabel(root, text='Employee management system', font=('peyda', 20, 'bold'), text_color='#07C6E0', bg_color='transparent')
headingLabel.place(x=20, y=100)

usernameEntry = CTkEntry(root, placeholder_text='Enter your username', width=250)
usernameEntry.place(x=20, y=150)

passwordEntry = CTkEntry(root, placeholder_text='Enter your password', show='*', width=250)
passwordEntry.place(x=20, y=200)

loginButton = CTkButton(root, text='Login', width=250, height=40, cursor='hand2', command=login)
loginButton.place(x=20, y=250)
  
root.mainloop()  