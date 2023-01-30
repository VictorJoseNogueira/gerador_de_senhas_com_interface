import tkinter
from tkinter import *
from tkinter import messagebox
from random import randint, choice
import os

arquivo = os.path.dirname(__file__)
nome_Do_arquivo_criado = arquivo+'\\gerador_de_senhas_automatico.txt'


class janela:

    def __init__(self, titulo='', lxa=''):
        self.dicionario = []
        self.janela = Tk()
        self.janela.title(titulo)
        self.janela.geometry(lxa)
        self.escrita = Label(self.janela, text='Gerador de senhas', anchor=N, background='#d3d3d3', font=('Arial', 15))
        self.escrita.place(x=50, y=10, height=30)
        self.escrita2 = Label(self.janela, text='Site:', anchor=W, background='#d3d3d3')
        self.escrita2.place(x=10, y=70, width=100, height=20)
        self.caixadetexto = Entry(self.janela)
        self.caixadetexto.place(anchor=W, x=55, y=80, width=200, height=20)
        self.escrita3 = Label(self.janela, text='Log-in:', anchor=W, background='#d3d3d3')
        self.escrita3.place(x=10, y=100, width=100, height=20)
        self.caixadetexto2 = Entry(self.janela)
        self.caixadetexto2.place(anchor=W, x=55, y=110, width=200, height=20)
        self.checkbutton = IntVar()
        self.check = tkinter.Checkbutton(self.janela, text='site permite caracteres especiais ?', variable=self.checkbutton)
        self.check.place(x=10, y=130)
        self.botao1 = self.botoes(self.janela,text='Gerar Senha', anchor=N, comando=self.senhar,x=10, y=170, width=100, height=30)
        self.botao2 = self.botoes(self.janela, text='Salvar Senha', anchor=N, comando=self.combinandofunc, x=10,y=200,width=100, height=30)
        self.botao3 = self.botoes(self.janela, text='mostrar senhas', anchor=N, comando=self.abridor, x=170, y=170, width=100, height=30)
        self.janela.config(background='#d3d3d3')
        self.janela.mainloop()
    def salvarsenhas(self):
        bancodesenhas = open(nome_Do_arquivo_criado, 'a')
        bancodesenhas.write(f'site: ' + self.caixadetexto.get()+'\n')
        bancodesenhas.write(f'login: ' + self.caixadetexto2.get() + '\n')
        bancodesenhas.write(f'Senha: ' + self.dicionario[0] + '\n')
        bancodesenhas.write('-' * 50 + ' \n')
        bancodesenhas.close()

    def delete(self):
        self.caixadetexto.delete(0, END)
        self.caixadetexto2.delete(0, END)

    def boxmsg(self):
        resp = messagebox.askquestion(title='Gerador', message='senha gerada com sucesso.\ndeseja continuar?')
        if resp == 'no':
            quit()
        elif resp == 'yes':
            self.delete()

        else:
            print('\033[31msomething goes wrong\033[m')

    def textos(self, local, text, anchor, x, y, width, height):
        Label(local, text=text, anchor=anchor).place(x=x, y=y, width=width, height=height)

    def caixatxts(self, local, anchor, x, y, width, height):
        Entry(local).place(anchor=anchor, x=x, y=y, width=width, height=height)

    def botoes(self, local, text, anchor, x, y, width, height, comando):
        Button(local, text=text, anchor=anchor, command=comando).place(x=x, y=y, width=width, height=height)

    def senhar(self):
        self.dicionario.clear()
        lista = ['!', '@', '#', '$', '%', '&', '*']
        listaa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'o', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u',
                  'v', 'w', 'x', 'y', 'z']
        senha = []
        if self.checkbutton.get() == 1:
            u = choice(lista)
            d = choice(listaa)
            t = choice(listaa)
            q = choice(listaa)
            g = choice(listaa)
            s = choice(listaa)
            se = randint(0, 9)
            o = randint(0, 9)
            senha.append(u)
            senha.append(d)
            senha.append(t)
            senha.append(q)
            senha.append(g)
            senha.append(s)
            var = str(se)
            senha.append(var)
            var1 = str(o)
            senha.append(var1)
            x = ''.join(senha)
            self.dicionario.append(x)
            print(x)
            messagebox.showinfo('Senha gerada', f'{x}')
        else:
            u = choice(listaa)
            d = choice(listaa)
            t = choice(listaa)
            q = choice(listaa)
            g = choice(listaa)
            s = choice(listaa)
            se = randint(0, 9)
            o = randint(0, 9)
            senha.append(u)
            senha.append(d)
            senha.append(t)
            senha.append(q)
            senha.append(g)
            senha.append(s)
            var = str(se)
            senha.append(var)
            var1 = str(o)
            senha.append(var1)
            x = ''.join(senha)
            self.dicionario.append(x)
            print(x)
            messagebox.showinfo('Senha gerada', f'{x}')

    def combinandofunc(self):
        if len(self.caixadetexto.get()) == 0:
            messagebox.showinfo('Site esta vazio', 'por favor digite o site')

        elif len(self.caixadetexto2.get()) == 0:
            messagebox.showinfo('log-in esta vazio', 'por favor digite o log-in')
        else:
            self.salvarsenhas()
            self.boxmsg()

    def abridor(self):
        os.startfile(nome_Do_arquivo_criado)


c = janela(titulo='Gerador.py', lxa='300x250')
