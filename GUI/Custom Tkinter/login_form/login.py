# import custom Tkinter

from customtkinter import *

app = CTk()

app.title("Login form")
app.geometry("400x300")

#btn create

btn = CTkButton(master=app,text="Click..",corner_radius=10)

btn.place(relx=0.5,rely=0.5,anchor='center')

app.mainloop()