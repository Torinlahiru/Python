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
    text="Welcome! Please click",
    text_color="white",  
    font=("Arial", 16)   
)


# btn create
 
btn = CTkButton(master=app,text="Click..",corner_radius=10,hover_color="#0ec3e3",fg_color="#066778",border_color="#50f03e",border_width=2)

 

label.place(relx=0.5, rely=0.3, anchor='center')   
btn.place(relx=0.5,rely=0.5,anchor='center')

app.mainloop()