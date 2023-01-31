import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from random import randint, choice
import os


class testejanela:
    def __init__(self, titulo='', tamanho=''):
        self.janela = Tk()
        self.janela.title(titulo)
        self.janela.geometry(tamanho)


z = testejanela(titulo='TAMANHO', tamanho="300x300")
z.janela.texto = Label(text='AFASFGAFAdfadafsfads')
z.janela.texto.place(x=110, y=20, height=200)
z.janela.mainloop()


y = testejanela(titulo='avemaria', tamanho='400x400')
y.janela.mainloop()
import sys
sys.platform
'win32'
import os
os.startfile(r'C:\Users\T-GAMER\Documents\meu_pc_projetos\gerador_de_senhas_com_interface\gerador\gerador_de_senhas_automatico.txt')
