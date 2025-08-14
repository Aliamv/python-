#!/usr/bin/env python3
from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database
import os
#functions
def delet_all():
    result = messagebox.askyesno('Confirm', 'Do you realy want to delet all the records?')
    if result : 
        database.deletall_records()
    else :
        pass
    treeview_data()
    

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')
    

def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter value to search') 
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error', 'Select an option')
    else :
        searched_data = database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
    for employee in searched_data:
        tree.insert('', END, values=employee)

def delet_employee():
    selected_item = tree.selection()
    if not selected_item :
        messagebox.showerror('Error', 'Select data to delet')
    else:
        item_values = tree.item(selected_item)['values']
        employee_id = item_values[0]
        
        database.delet(employee_id)
        treeview_data()
        clear()
        messagebox.showerror('Error', 'data is deleted')
    


def update_employee():
    selected_item = tree.selection()
    if not selected_item :
        messagebox.showerror('Error', 'Select data to update')
    elif not salaryEntry.get().replace('.', '').isdigit():
        messagebox.showerror('Error', 'Salary must be a number')
        return
    else:
        item_values = tree.item(selected_item)['values']
        employee_id = item_values[0]

        database.update(employee_id
        ,nameEntry.get()
        ,phoneEntry.get()
        ,roleBox.get()
        ,genderBox.get()
        ,salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is updated')
    
def selection(event):
    clear()
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value = False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0, END)

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

def add_employee():
    if (idEntry.get() == '' or
        nameEntry.get() == '' or 
        phoneEntry.get() == '' or
        roleBox.get() == '' or
        genderBox.get() == '' or
        salaryEntry.get() == ''):
        messagebox.showerror('Error', 'All fields are required')
    elif not salaryEntry.get().isdigit():
        messagebox.showerror('Error', 'Salary must be a number')
    elif  database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists')
    else: 
        database.insert(
            idEntry.get(),
            nameEntry.get(),
            phoneEntry.get(),
            roleBox.get(),
            genderBox.get(),
            salaryEntry.get()
        )
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is added')
    


#UI
window = CTk()
window.geometry('930x580+100+100')
window.configure(fg_color = '#6C90FE')
window.resizable(0,0)
window.title('Employee management system')
logo = CTkImage(Image.open('employee.jpg'), size=(930,165))
logoLabel = CTkLabel(window,image=logo,text="")
logoLabel.grid(row = 0, column = 0, columnspan = 2)

leftFrame = CTkFrame(window,fg_color = '#6C90FE')
leftFrame.grid(row = 1,column = 0)

idLabel = CTkLabel(leftFrame,text='ID', font=('peyda', 18, 'bold'), text_color='#122A36')
idLabel.grid(row=0, column=0, padx=20,pady=15, sticky = 'w')
idEntry = CTkEntry(leftFrame,width= 180, font=('peyda', 15, 'bold'))
idEntry.grid(row = 0 , column = 1)

nameLabel = CTkLabel(leftFrame,text='Name', font=('peyda', 18, 'bold'), text_color='#122A36')
nameLabel.grid(row=1, column=0, padx=20,pady=15, sticky = 'w')
nameEntry = CTkEntry(leftFrame,width= 180, font=('peyda', 15, 'bold'))
nameEntry.grid(row = 1 , column = 1)

phoneLabel = CTkLabel(leftFrame,text='Phone', font=('peyda', 18, 'bold'), text_color='#122A36')
phoneLabel.grid(row=2, column=0, padx=20,pady=15, sticky = 'w')
phoneEntry = CTkEntry(leftFrame,width= 180, font=('peyda', 15, 'bold'))
phoneEntry.grid(row = 2 , column = 1)

roleLabel=CTkLabel(leftFrame, text='Role' ,font=('arial' ,18, 'bold'), text_color='#122A36')
roleLabel.grid(row=3,column=0,padx=20, pady=15, sticky='w')
role_options=[ 'Web Developer', 'Cloud Architect', 'Technical Writer', 'Network Engineer',
'Data Scientist', 'Business Analyst', 'IT Consultant', 'UX/UI Designer', 'DevOps Engineer']
roleBox=CTkComboBox(leftFrame, values=role_options, width=180,font=('peyda', 15, 'bold'), state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame, text='Gender' ,font=('arial' ,18, 'bold'), text_color='#122A36')
genderLabel.grid(row=4,column=0,padx=20, pady=15, sticky='w')
gender_options= ['Male', 'Female']
genderBox=CTkComboBox(leftFrame, values=gender_options, width=180,font=('peyda', 15, 'bold'),state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set(gender_options[0])

salaryLabel = CTkLabel(leftFrame,text='Salary', font=('peyda', 18, 'bold'), text_color='#122A36')
salaryLabel.grid(row=5, column=0, padx=20,pady=15, sticky = 'w')
salaryEntry = CTkEntry(leftFrame,width= 180, font=('peyda', 15, 'bold'))
salaryEntry.grid(row = 5 , column = 1)




rightFrame = CTkFrame(window)
rightFrame.grid(row = 1,column = 1)


search_options = ['Id', 'Name', 'Role', 'Gender', 'Salary' ]
searchBox=CTkComboBox(rightFrame , values=search_options,   state='readonly')
searchBox.grid(row=0, column=0 )
searchBox.set('Search by')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row = 0, column = 1)
 
searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2, padx=(10, 5), pady=5, sticky='ew')

showAllButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showAllButton.grid(row=0, column=3, padx=(5, 10), pady=5, sticky='ew')

rightFrame.grid_columnconfigure(2, weight=1)
rightFrame.grid_columnconfigure(3, weight=1)

tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4, sticky='nsew')
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_columnconfigure(0, weight=1)
tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')

tree.heading('Id', text= 'Id')
tree.heading('Name', text= 'Name')
tree.heading('Phone', text= 'Phone')
tree.heading('Role', text= 'Role')
tree.heading('Gender', text= 'Gender')
tree.heading('Salary', text= 'Salary')

tree.config(show='headings')

tree.column('Id', width=90, anchor='center', stretch=True)
tree.column('Name', width=130, anchor='center', stretch=True)
tree.column('Phone', width=120, anchor='center', stretch=True)
tree.column('Role', width=120, anchor='center', stretch=True)
tree.column('Gender', width=60, anchor='center', stretch=True)
tree.column('Salary', width=80, anchor='center', stretch=True)

style = ttk.Style()
style.configure('Treeview.Heading', font=('peyda', 18)) 
style.configure('Treeview', font=('peyda', 15),rowheight = 30, background = '#6C90FE',foreground='white')

scrollBar = ttk.Scrollbar(rightFrame, orient='vertical', command=tree.yview) 
scrollBar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=scrollBar.set)

buttonFrame = CTkFrame(window, fg_color = '#6C90FE')
buttonFrame.grid(row = 2, column = 0, columnspan = 2)

newButton = CTkButton(buttonFrame, text='New Employee', font=('peyda', 15, 'bold'), width=160, command=lambda:clear(True))
newButton.grid(row = 0, column = 0, pady = 10)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('peyda', 15, 'bold'), width=160, command=add_employee)
addButton.grid(row = 0, column = 1, pady = 10, padx = 5) 

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('peyda', 15, 'bold'), width=160, command=update_employee)
updateButton.grid(row = 0, column = 2, pady = 10, padx = 5)

deletButton = CTkButton(buttonFrame, text='Delet Employee', font=('peyda', 15, 'bold'), width=160, command=delet_employee)
deletButton.grid(row = 0, column = 3, pady = 10, padx = 5)

deletAllButton = CTkButton(buttonFrame, text='Delet All', font=('peyda', 15, 'bold'), width=160 , command=delet_all)
deletAllButton.grid(row = 0, column = 4, pady = 10, padx = 5)

try:
    with open('current_role.txt', 'r') as f:
        user_role = f.read().strip()
except Exception:
    user_role = 'admin'

if user_role == 'po':
    deletButton.configure(state=DISABLED)
    deletAllButton.configure(state=DISABLED)
elif user_role == 'clerk':
    addButton.configure(state=DISABLED)
    updateButton.configure(state=DISABLED)
    deletButton.configure(state=DISABLED)
    deletAllButton.configure(state=DISABLED)
    newButton.configure(state=DISABLED)

    tree['displaycolumns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender')

    idEntry.configure(state=DISABLED)
    nameEntry.configure(state=DISABLED)
    phoneEntry.configure(state=DISABLED)
    roleBox.configure(state=DISABLED)
    genderBox.configure(state=DISABLED)
    salaryEntry.configure(state=DISABLED)

treeview_data()
tree.bind('<<TreeviewSelect>>', selection)
window.mainloop()
