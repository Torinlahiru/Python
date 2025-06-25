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

url = tk.Entry(root,width=50)
url.pack(pady=10)

btn = tk.Button(root,text="Short",bg="#007ACC",fg="white")
btn.pack(pady=10)


result = tk.Label(root,text="Result",width=50,fg="#007ACC")
result.pack(pady=5)
root.mainloop()