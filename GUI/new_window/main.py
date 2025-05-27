from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New windows")
root.geometry('300x400')

top = Toplevel()

Label(top, text="Welcome").pack()

# Open original image
img_path = r"G:\My projects\python\Python\GUI\new_window\car.png"
original_img = Image.open(img_path)

# Resize the image (width, height)
size = (400, 400)
img_resized = original_img.resize(size)

# Convert resized image to PhotoImage
img_tk = ImageTk.PhotoImage(img_resized)

# Display resized image in Label
lbl2 = Label(top, image=img_tk)
lbl2.image = img_tk  # Keep reference!
lbl2.pack()

root.mainloop()
