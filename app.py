from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
frame1.place(x=0, y=0)

Label(root, text='Language Translator', font=('Helvetica 20 bold'), fg="black", bg='#F7DC6F').pack(pady=10)

text_entry1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1= Button(frame1, text='Translate', relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor='hand2')
btn1.place(x=185, y=300)

btn2= Button(frame1, text='Clear', relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor='hand2')
btn2.place(x=300, y=300)

root.mainloop()