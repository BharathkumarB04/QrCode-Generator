import customtkinter as c
import pyqrcode as q
from tkinter import *
from PIL import Image
from tkinter import messagebox as mb
from tkinter import filedialog as f

#function
def submit():
        link = inp.get()
        if not link:
             mb.showwarning("Warning","Fill his field!")
        else:
            qr = q.create(link)
            qr.png("qrcode.png", scale=5)
            mb.showinfo("Success","QR Code generated sucessfully..")
        
def show():
    try:
        if((inp.get())==""):
            mb.showerror("Error","Qrcode not found,Generate first!")
        else:
            img = Image.open("qrcode.png")
            img.show()  
    except FileNotFoundError:
         mb.showerror("Error","Qrcode not found,Generate first!")

def Reset():
    inp.set('')

def save():
    try:
        if (inp.get()==""):
             mb.showwarning("Error","No Qrcode Found!")
        else:
            img = Image.open("qrcode.png")
            save_path = f.asksaveasfile(defaultextension=".jpg", filetypes=[("All files",'*.*'),("PNG Files","*.png"),("JPG Files","*.jpg"),("JPEG Files","*.jpeg"),("JPE Files","*.jpe"),("BMP Files","*.bmp")], title="Save As", mode='wb')
            if (save_path):
                img.save(save_path)
                save_path.close()
                mb.showinfo("Saved","Qrcode saved sucessfully..")
    except FileNotFoundError:
         mb.showerror("Error","QR code not found. Please Generate first!")

#Screen
root = c.CTk() #Screen initialization
root.geometry("350x210")
root.title("QR code generator")
root.resizable(False, False)

#labels
c.CTkLabel(root, text=" QR CODE GENERATOR", font=("TIMES NEW ROMAN BOLD",26), fg_color="light blue", text_color="blue", corner_radius=15).place(x=10,y=10)
c.CTkLabel(root, text="Enter the link : ").place(x=10, y=80)

#entry
inp = StringVar(root)
entry = c.CTkEntry(root, width=200, textvariable=inp).place(x=100, y=80)

#buttons
btn = c.CTkButton(root, text="Generate", width =35, command= submit).place(x=50, y=140)
btn2 = c.CTkButton(root, text="Preview", width=35, command=show ).place(x=125, y=140)
btn3 = c.CTkButton(root, text="Reset", width=35, command=Reset ).place(x=185, y=140)
btn3 = c.CTkButton(root, text="Save As", width=35, command=save ).place(x=240, y=140)

#declaration
root.mainloop()