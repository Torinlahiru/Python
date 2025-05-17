# import custom Tkinter

from customtkinter import *

# import pillow

from PIL import *


app = CTk()

app.title("Login form")
app.geometry("400x300")

# change light/dark mode
set_appearance_mode('dark')

# Add a label
label = CTkLabel(
    master=app,
    text="Welcome!",
    text_color="white",  
    font=("Arial", 16)   
)

# Add a username field (entry)
username = CTkEntry(
    master=app,
    placeholder_text="Username"
)
# Add a password field (entry)
password = CTkEntry(
    master=app,
    placeholder_text="Password",
    show="*"
)

# login function
def login():
    if username.get() == "admin" and  password.get() == "1234":
        "Success"
    else:
        return "Error"

# btn create
 
btn = CTkButton(master=app,text="Log In",
                corner_radius=10,
                hover_color="#0ec3e3",
                fg_color="#066778",
                border_color="#50f03e",
                border_width=2,
                command=login)

btn_close = CTkButton(master=app,text="Close",
                      corner_radius=10,
                      hover_color="#0ec3e3",
                      fg_color="#066778",
                      border_color="#50f03e",
                      border_width=2)

 

label.place(relx=0.5, rely=0.3, anchor='center')   
username.place(relx=0.5, rely=0.4, anchor='center')
password.place(relx=0.5, rely=0.5, anchor='center')
btn.place(relx=0.5,rely=0.6,anchor='center')
btn_close.place(relx=0.5,rely=0.7,anchor='center')

app.mainloop()

