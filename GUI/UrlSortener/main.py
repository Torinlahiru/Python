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

# Function url shorten
def shorten_url():
    long_url = url.get().strip()
    if not long_url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    
    api_url = "http://tinyurl.com/api-create.php"
    params = {'url': long_url}
    
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            short_url = response.text
            result.config(text=short_url)
            pyperclip.copy(short_url)
            messagebox.showinfo("Success", "Short URL copied to clipboard!")
        else:
            messagebox.showerror("API Error", f"Failed to shorten URL. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")
