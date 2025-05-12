import tkinter
from tkinter import messagebox

root = tkinter.Tk()

root.title ="Login Form"
root.geometry('400x400')
root.configure(bg='#333333')

# Frame create

frame =tkinter.Frame(bg='#333333')

# login function

def login():
    username = "lahiru"
    password = "12345"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Success",message="Successfully logged !")
         
    else:
         
        messagebox.showerror(title="Error",message='Invalid user or password ! ')
        


# Widgets 
login_label = tkinter.Label(frame,text="Login Form",bg='#333333',foreground='#ffffff',font=("Arial",30))
username = tkinter.Label(frame,text="Username",bg='#333333',foreground='#ffffff',font=("Arial",16))
username_entry = tkinter.Entry(frame,font=("Arial",16))
password = tkinter.Label(frame,text="Password",bg='#333333',foreground='#ffffff',font=("Arial",16))
password_entry = tkinter.Entry(frame,show="*",font=("Arial",16))

btn_login = tkinter.Button(frame,text="Log In",bg='#d9c725',foreground='#ffffff' ,font=("Arial",16),command=login)

# Place widgets

login_label.grid(row=0,column=2,sticky='news',pady=14)
username.grid(row=1,column=1)
username_entry.grid(row=1,column=2,pady=20)
password.grid(row=2,column=1)
password_entry.grid(row=2,column=2,pady=20)

btn_login.grid(row=3,column=2,pady=30)

frame.pack()
root.mainloop()