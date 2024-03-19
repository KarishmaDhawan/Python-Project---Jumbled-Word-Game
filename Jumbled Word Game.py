from tkinter import *
import random
from tkinter import messagebox

real_word= [
    "ADULT",
    "INDIA",
    "AGENT",
    "BASIS",
    "BIRTH",
    "BLOCK",
    "BLOOD",
    "DRESS",
    "EARTH",
    "ALLOW",
    "AGREE",
    "AVOID",
    "BRAVE",
    "BLIND",
    "BIRDS"
]
jumbled_word= [
    'UTLDA',
    'DIANI',
    'GENTA',
    'SISBA',
    'RTHBI',
    'OCKBL',
    'BOLDO',
    "RESSD",
    "RTHEA",
    "LOWAL",
    "EERGA",
    "OIDAV",
    "RAVEB",
    "DLINB",
    "SRDIB"
]

options = random.randrange(0,len(jumbled_word),1)

def one():
    global jumbled_word, real_word , options
    lbl1.config(text=jumbled_word[options])

def answer():
    global jumbled_word, real_word , options
    options = random.randrange(0,len(jumbled_word),1)
    lbl1.config(text=jumbled_word[options])
    e1.delete(0,END)

def correct():
    global jumbled_word, real_word , options
    one_var = e1.get()
    if one_var == real_word[options]:
        messagebox.showinfo("Congratulations!!"," Your answer is correct....well done !")
        answer()
    else: 
        messagebox.showinfo("Sorry!!","Try better next time :)")
        e1.delete(0,END)

window = Tk()
window.geometry("350x400+400+300")
window.title("Jumbled Word Game")
window.configure(background = "purple")

lbl1= Label(window, text = 'WRITE HERE', font= ("Arial",30,"bold") , bg= "white", fg = "red")
lbl1.pack(pady = 30 , ipady = 10 , ipadx = 10)
correct_1 = StringVar()
e1=Entry(window, font =("arial",25,"bold"),textvariable= correct_1)
e1.pack(ipady=5 , ipadx = 5)

correct_button = Button(window, text="CHECK OUT", font=("arial",20,"bold"), width =20 , bg = "white",fg = "black", relief= GROOVE , command = correct)
correct_button.pack(pady=40)
    
reset_button= Button(window, text='RESET', font = ('arial', 20 , 'bold'), width = 20 , bg = "white", fg = "black" , relief= GROOVE , command =answer)
reset_button.pack()

one()


window.mainloop()