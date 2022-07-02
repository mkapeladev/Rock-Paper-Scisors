import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time

from PIL.ImageTk import PhotoImage

uin = 0
uw = 0
aiw = 0
r = 0
a = 0
t = 1
ain = random.randrange(1,4)
root = tk.Tk()
def Win():
    root.title("Kamień Papier Nożyce")
    root.iconbitmap('C:/Users/Maciej/Downloads/rock.ico')
    root.geometry("600x400")
    root.config(bg="white")
def Rockc(event):
    global a, uin , r , uw , aiw
    a = 1
    uin = 1
    rocklabel.config(bg="blue")
    messagebox.showinfo("Wybór", "Twoim wyborem jest kamień")
    scisorlabel.config(image="")
    paperlabel.config(image="")
    if ain == 1:
        paperlabel.config(image=renderr)
        rocklabel.config(bg="white")
        messagebox.showinfo("Wybór", "Remis")
        paperlabel.config(bg="yellow")
        rocklabel.config(bg="yellow")
        scisorlabel.config(image=renderpit)
        r +=1
    elif ain == 2:
        paperlabel.config(image=renders)
        rocklabel.config(bg="white")
        messagebox.showinfo("Wybór", "Wygrana")
        rocklabel.config(bg="green")
        paperlabel.config(bg="red")
        scisorlabel.config(image=renderpuchar)
        uw +=1
    elif ain == 3:
        paperlabel.config(image=renderp)
        rocklabel.config(bg="white")
        messagebox.showinfo("Wybór", "Przegrana")
        rocklabel.config(bg="red")
        paperlabel.config(bg="green")
        scisorlabel.config(image=rendersad)
        aiw +=1
def Rockle(event):
    if a != 1:
        rocklabel.config(bg="yellow")
def Rocklex(event):
    if a != 1:
        rocklabel.config(bg="white")
def Edwardc(event):
    global a, uin , r , uw , aiw
    uin = 2
    a = 1
    scisorlabel.config(bg="blue")
    rocklabel.config(image="")
    paperlabel.config(image="")
    messagebox.showinfo("Wybór", "Twoim wyborem są nożyce")
    if ain == 1:
        paperlabel.config(image=renderr)
        scisorlabel.config(image="", bg="white")
        rocklabel.config(image=renders)
        messagebox.showinfo("Wynik", "Przegrana")
        rocklabel.config(bg="red")
        paperlabel.config(bg="green")
        scisorlabel.config(image=rendersad)
        aiw += 1

    elif ain == 2:
        paperlabel.config(image=renders)
        scisorlabel.config(image="", bg="white")
        rocklabel.config(image=renders)
        messagebox.showinfo("Wynik", "Remis")
        rocklabel.config(bg="yellow")
        paperlabel.config(bg="yellow")
        scisorlabel.config(image=renderpit)
        r +=1
    elif ain ==3:
        paperlabel.config(image=renderp)
        scisorlabel.config(image="", bg="white")
        rocklabel.config(image=renders)
        messagebox.showinfo("Wynik", "Wygrana")
        scisorlabel.config(image=renderpuchar)
        rocklabel.config(bg="green")
        paperlabel.config(bg="red")
        uw +=1
def Edwardle(event):
    if a != 1:
        scisorlabel.config(bg="yellow")
def Edwardex(event):
    if a != 1:
        scisorlabel.config(bg="white")
def Paperc(event):
    global a, uin, r , uw , aiw
    a = 1
    uin = 3
    paperlabel.config(bg="blue")
    messagebox.showinfo("Wybór", "Twoim wyborem jest Papier")
    rocklabel.config(image="")
    scisorlabel.config(image="")
    paperlabel.config(bg="White")
    if ain == 1:
        rocklabel.config(image=renderp)
        paperlabel.config(image=renderr)
        messagebox.showinfo("Wygrana", "Wygrana")
        paperlabel.config(bg="red")
        rocklabel.config(bg="green")
        scisorlabel.config(image=renderpuchar)
        uw +=1
    elif ain == 2:
        rocklabel.config(image=renderp)
        paperlabel.config(image=renders)
        messagebox.showinfo("Przegrana", "Przegrana")
        paperlabel.config(bg="green")
        rocklabel.config(bg="red")
        scisorlabel.config(image=rendersad)
        aiw +=1

    elif ain == 3:
        rocklabel.config(image=renderp)
        messagebox.showinfo("Remis", "Remis")
        rocklabel.config(bg="yellow")
        paperlabel.config(bg="yellow")
        scisorlabel.config(image=renderpit)
        r +=1
def Papere(event):
    if a != 1:
        paperlabel.config(bg="yellow")
def Paperex(event):
    if a != 1:
        paperlabel.config(bg="white")
def Score(event):
    global t, r , uw , aiw

    messagebox.showinfo("Wyniki",f"Lącznie gier było {t} \n Gier Wygrałeś:{uw}  \n Gier Przegrałeś: {aiw} \n  Remisów było: {r}" )
def Clear(event):
    global a , ain ,t
    a = 0
    ain = random.randrange(1,4)
    paperlabel.config(bg="White",image=renderp)
    rocklabel.config(bg="White", image=renderr)
    scisorlabel.config(bg="white", image=renders)
    t += 1

piterimg = Image.open("../Tic-Tac-toe/neut.png")
piterimg = piterimg.resize((284, 178) , Image.ANTIALIAS)
renderpit = ImageTk.PhotoImage(piterimg)
sadfaceimg = Image.open("../Tic-Tac-toe/sad face.png")
sadfaceimg = sadfaceimg.resize((284, 178), Image.ANTIALIAS)
rendersad = ImageTk.PhotoImage(sadfaceimg)
rockimg = Image.open("../Tic-Tac-toe/rockBg.png")
rockimg = rockimg.resize((284, 178), Image.ANTIALIAS)
renderr: PhotoImage = ImageTk.PhotoImage(rockimg)
rocklabel= tk.Label(root, image=renderr, width=150, height=250, bg="white")
rocklabel.place(x=50, y=80)
rocklabel.bind('<Enter>', Rockle)
rocklabel.bind('<Leave>', Rocklex)
rocklabel.bind('<Button>', Rockc)
pucharimg = Image.open("../Tic-Tac-toe/puchar.png")
pucharimg = pucharimg.resize((284, 178), Image.ANTIALIAS)
renderpuchar = ImageTk.PhotoImage(pucharimg)
scisorimg= Image.open("../Tic-Tac-toe/nozycer.png")
scisorimg = scisorimg.resize((284 ,178), Image.ANTIALIAS)
renders = ImageTk.PhotoImage(scisorimg)
scisorlabel = tk.Label(root , image=renders , width=150 ,height=250, bg="white")
scisorlabel.place(x= 220 , y= 80)
scisorlabel.bind('<Enter>', Edwardle)
scisorlabel.bind('<Leave>', Edwardex)
scisorlabel.bind('<Button>', Edwardc)
paperimg = Image.open("../Tic-Tac-toe/papier.png")
renderp = ImageTk.PhotoImage(paperimg)
paperimg = paperimg.resize((284 ,178), Image.ANTIALIAS)
paperlabel= tk.Label(root, image=renderp, width=150, height=250, bg="white")
paperlabel.bind('<Enter>', Papere)
paperlabel.bind('<Leave>', Paperex)
paperlabel.bind('<Button>', Paperc)
paperlabel.place(x=400, y=80)
root.bind("<space>",Clear)
root.bind("<Tab>",Score)
Win()
root.mainloop()