import random
import json
import os

import tkinter as tk
from tkinter import simpledialog

# GUI
ROOT = tk.Tk()

ROOT.withdraw()

# Adding color and size to the root

# the input dialog
usage = simpledialog.askstring(title="Password-Archive APP",
                                  prompt="Where you are going to use this password? [One-Two word]")

passlen = int(simpledialog.askstring(title="Password-Archive APP",
                                  prompt="Enter the length of password: "))

# BACKEND
f_name = "password-archive.json"

seq ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passwrd = "".join(random.sample(seq,passlen))
	
dictionary = {usage: passwrd}

files = os.listdir(".")

if(f_name not in files):
	with open(f_name,'w') as jf:
		json.dump(dictionary,jf)
else:
	with open(f_name,'r+') as jf:
		data = json.load(jf)
		data.update(dictionary)
		jf.seek(0)
		json.dump(data,jf,indent=2)

print(dictionary)	



