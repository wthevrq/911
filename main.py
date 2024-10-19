<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">             
   <title>000</title>
</head>
<body>

import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import urllib.parse

def pindah_button(button):
    new_x = random.randint(0, window.winfo_width() - button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - button.winfo_height())
    button.place(x=new_x, y=new_y)

def tekan_ya():
    messagebox.showinfo("WARNING!!!", "bye nak majok,tahulah dh tk sayang")
    buka_whatsapp()

def tekan_tidak():
    pindah_button(tidak_button)

def buka_whatsapp():
    encoded_message = urllib.parse.quote(pesan)
    webbrowser.open_new(f"https://api.whatsapp.com/send?phone=60166745878&text=🗿.")

window = tk.Tk()
window.title("000")
window.geometry("400x600")
window.configure(bg='#c0d6ff')  

frame = tk.Frame(window, bg='c0d6ff', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="Sayang saya takk?", font=("Helvetica", 16, "bold"), bg='#c0d6ff', fg='#8489d8', justify=tk.CENTER)
label.pack(pady=20)

ya_button = tk.Button(frame, text="TAK", font=("Helvetica", 14), command=tekan_ya, bg='#8489d8', fg='white', width=8)
ya_button.pack(side=tk.LEFT, padx=10)

tidak_button = tk.Button(window, text="IYE", font=("Helvetica", 14), command=tekan_tidak, bg='#8489d8', fg='white', width=8)
tidak_button.place(x=50, y=50)

window.mainloop()
</body>
</html>
