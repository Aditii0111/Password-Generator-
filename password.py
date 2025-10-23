import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_characters = uppercase + lowercase + digits + symbols
    password += [secrets.choice(all_characters) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def on_generate():
    try:
        length = int(entry.get())
        pwd = generate_password(length)
        result_label.config(text=pwd)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# GUI setup
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Generate Password", command=on_generate, font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()
