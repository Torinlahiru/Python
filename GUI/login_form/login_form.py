import tkinter

root = tkinter.Tk()

root.title ="Login Form"
root.geometry('400x400')
root.configure(bg='#333333')

# Widgets 
login_label = tkinter.Label(root,text="Login Form")
username = tkinter.Label(root,text="Username")
username_entry = tkinter.Entry(root)
password = tkinter.Label(root,text="Password")
password_entry = tkinter.Entry(root,show="*")

btn_login = tkinter.Button(root,text="Log In")

# Place widgets

login_label.grid(row=0,column=2)
username.grid(row=1,column=1)
username_entry.grid(row=1,column=2)
password.grid(row=2,column=1)
password_entry.grid(row=2,column=2)

btn_login.grid(row=3,column=2)


root.mainloop()