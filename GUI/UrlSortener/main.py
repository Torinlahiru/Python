import tkinter as tk
import requests
from tkinter import messagebox
import pyperclip

# Gui section

root = tk.Tk()
root.title("URL Shortener")
root.geometry('400x400')

lbl = tk.Label(root,text="Enter URL ..",font=("Arial",14))
lbl.pack(pady=10)
root.mainloop()