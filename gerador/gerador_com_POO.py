from tkinter import *
from tkinter import messagebox
import os

arquivo = os.path.dirname(__file__)
nome_Do_arquivo_criado = arquivo+'\\gerador_de_senhas_automatico.txt'

def salvarsenhas():
    bancodesenhas = open(nome_Do_arquivo_criado, 'a')
    bancodesenhas.write(f'site:  \n')
    bancodesenhas.write(f'login: \n')
    bancodesenhas.write(f'Senha: \n')
    bancodesenhas.write('-'*50+'\n')
    bancodesenhas.close()
def textbotao():
    messagebox.showinfo('Teste', 'Senha gerada')

def textos(local, text, anchor, x, y, width, height):
    Label(local, text=text, anchor=anchor).place(x=x, y=y, width=width, height=height)


def caixatxts(local, anchor, x, y, width, height):
    Entry(local).place(anchor=anchor, x=x, y=y, width=width, height=height)


def botoes(local, text, anchor, x, y, width, height, comando):
    Button(local, text=text, anchor=anchor, command=comando).place(x=x, y=y, width=width, height=height)


class janela:
    def __init__(self, titulo='', lxa=''):
        self.janela = Tk()
        self.janela.title(titulo)
        self.janela.geometry(lxa)
        self.janela.textos = textos(self.janela,'Gerador de senhas', anchor=N, x=200, y=10, width=100, height=20)
        self.janela.textos2 = textos(self.janela,'Site', anchor=N, x=200, y=30, width=100, height=20)
        self.janela.caixadecriacao = caixatxts(self.janela, anchor=N, x=250, y=50, width=200, height=20)
        self.janela.textos3 = textos(self.janela,'Login', anchor=N, x=200, y=70, width=100, height=20)
        self.janela.caixatxt2 = caixatxts(self.janela, anchor=N, x=250, y=90, width=200, height=20)
        self.janela.botao1 = botoes(self.janela, text='Gerar e salvar', anchor=W, comando=textbotao, x=200, y=150, width=80, height=20)
        self.janela.botao2 = botoes(self.janela, text='salvando senha', anchor=W, comando=salvarsenhas, x=200, y=190, width=100, height=20)
        self.janela.mainloop()


c = janela(titulo='Gerador.py', lxa='500x500')
