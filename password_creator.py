import random
import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# GUI
ROOT = tk.Tk()
ROOT.withdraw()

# the input dialog
usage = simpledialog.askstring(title="Password-Archive APP",
                               prompt="Where are you going to use this password? [One-Two words]")

if usage is None:
    messagebox.showinfo("Password-Archive APP", "No usage provided. Exiting.")
    exit()

try:
    passlen = int(simpledialog.askstring(title="Password-Archive APP",
                                         prompt="Enter the length of the password: "))
except (TypeError, ValueError):
    messagebox.showinfo("Password-Archive APP", "Invalid password length. Exiting.")
    exit()

# Ensure password length is within the valid range
seq = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
if passlen > len(seq):
    messagebox.showinfo("Password-Archive APP", f"Password length cannot exceed {len(seq)}. Exiting.")
    exit()

# BACKEND
f_name = "password-archive.json"

# Generate the password
passwrd = "".join(random.sample(seq, passlen))

# Create the dictionary
dictionary = {usage: passwrd}

# Check if the file exists and update or create it
if not os.path.exists(f_name):
    with open(f_name, 'w') as jf:
        json.dump(dictionary, jf)
else:
    with open(f_name, 'r+') as jf:
        try:
            data = json.load(jf)
        except json.JSONDecodeError:
            data = {}
        data.update(dictionary)
        jf.seek(0)
        json.dump(data, jf, indent=2)

print(dictionary)
