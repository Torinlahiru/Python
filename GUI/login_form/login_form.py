import tkinter

root = tkinter.Tk()

root.title ="Login Form"
root.geometry('400x400')
root.configure(bg='#333333')

login_label = tkinter.Label(root,text="Login Form")
username = tkinter.Label(root,text="Username")
username_entry = tkinter.Entry(root)
password = tkinter.Label(root,text="Password")
password_entry = tkinter.Entry(root,show="*")

btn_login = tkinter.Button(root,text="Log In")


root.mainloop()