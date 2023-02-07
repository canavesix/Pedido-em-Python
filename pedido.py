
from email import message
import tkinter as tk 
import random 

root = tk.Tk()
root.geometry('200x200')

def hover(event):
    x = random.randint(0,200)
    y = random.randint(0,200)
    nao.place(x=x, y=y)

def mensagem():
    message = tk.Label(root, text='<3 <3 <3')
    message.place(x=70, y=120, relx=0, rely=0)

pergunta = tk.Label(root, text='Aceita namorar comigo?')
pergunta.pack(anchor='n', padx=20)

nao = tk.Button(root,text='Não')
nao.place(x=140, y=80)
nao.bind('<Enter>',hover)

sim = tk.Button(root, text='Sim', command= mensagem)
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop()

