# QRCode Generator
# Author: Raagul26
# Simple program to generate custom QRcode with more features

from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
from qrcode import QRCode
import os

# Main window
window = Tk()
window.iconphoto(False,PhotoImage(file='qr-code.png'))
window.title('QRCODE GENERATOR')
window.minsize(280, 350)
window.maxsize(600, 400)
window.geometry('500x400')


# Style
style = ttk.Style()
style.configure('TLabel', font=('comic sans ms', 11))
style.configure('TButton', font=('comic sans ms', 11), background="aqua")

# Label 1
l = ttk.Label(window, text="Content (Eg:Text,URL): ")
l.pack(pady=10)
content = StringVar()
e = ttk.Entry(window, text=content)
e.pack(fill=BOTH, padx=15, pady=10)
e.focus_force()

# Label 2
l1 = ttk.Label(window, text="Version: ")
l1.pack()
v = ttk.Combobox(window, values=list(range(1, 41)))
v.set(4)
v.pack(pady=5)

# Label 3
l2 = ttk.Label(window, text="Size (410 x 410):")
l2.pack()
s = ttk.Combobox(window, values=list(range(1, 100)))
s.set(10)
s.pack(pady=5)

# Label 4
l3 = ttk.Label(window, text="Border:")
l3.pack()
b = ttk.Combobox(window, values=list(range(1, 31)))
b.set(4)
b.pack(pady=5)

# Get home directory
home = os.path.expanduser('~')


# QRcode generate function
def qrgen(data, ver, box, border):
    # Get save as filename
    filename = filedialog.asksaveasfilename(initialdir=home, title='Save As', filetypes=(("PNG Files", "*.png"),
                                                                                         ("JPG Files", "*.jpg"),
                                                                                         ("All Files", "*.*")))
    if filename != "":
        qr = QRCode(
            version=ver,
            box_size=box,
            border=border)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(filename)
        img.get_image()
        messagebox.showinfo("Saved", "QRCode Saved Successfully")
    else:
        messagebox.showerror('Not Saved', 'QRCode Not Saved')


# Function to Invoke and get inputs
def generate():
    d = content.get()
    if d == "":
        messagebox.showwarning("QRCODE", "Invalid Input")
    elif d != "":
        ver = v.get()
        box = s.get()
        border = b.get()
        qrgen(d, ver, box, border)
        quit()


# Generate and Save Button
photo = PhotoImage(file='generate.png')
gen = ttk.Button(window, image=photo, command=generate)
gen.pack(pady=15)

# Label 4
l4 = ttk.Label(window, text="GENERATE")
l4.pack()

# mainloop
window.mainloop()
