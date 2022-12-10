from tkinter import *
#from tkinter import messagebox
#import os


def textos(local, text, anchor, x, y, width, height):
    Label(local, text=text, anchor=anchor).place(x=x, y=y, width=width, height=height)


class janela:
    def __init__(self, titulo='', lxa=''):
        self.janela = Tk()
        self.janela.title(titulo)
        self.janela.geometry(lxa)
        self.janela.textos = textos(self.janela,'Gerador de senhas', anchor=N, x=200, y=10, width=100, height=20)
        self.janela.mainloop()


c = janela(titulo='nem q a vaca tussa', lxa='500x500')
