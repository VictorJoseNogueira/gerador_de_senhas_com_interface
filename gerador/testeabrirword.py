import random
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import os
import pyperclip
import string

arquivo = os.path.dirname(__file__)
nome_Do_arquivo_criado = arquivo+'\\gerador_de_senhas_automatico.txt'


class janela:

    def __init__(self, titulo='', lxa=''):
        self.dicionario = []
        # interface
        self.janela = Tk()
        self.janela.title(titulo)
        self.janela.geometry(lxa)

        # Image
        self.image = PhotoImage(file="matrix.gif")
        self.background_label = Label(self.janela, image=self.image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #escritas
        self.escrita = Label(self.janela, text='Gerador de senhas', anchor=N, background='#d3d3d3', font=('Arial', 15))
        self.escrita.place(x=50, y=10, height=30)

        #escrita2
        self.escrita2 = Label(self.janela, text='Site:', anchor=W, background='#d3d3d3')
        self.escrita2.place(x=10, y=70, width=100, height=20)

        #caixas de texto
        self.caixadetexto = Entry(self.janela)
        self.caixadetexto.place(anchor=W, x=55, y=80, width=200, height=20)

        #escritas3
        self.escrita3 = Label(self.janela, text='Log-in:', anchor=W, background='#d3d3d3')
        self.escrita3.place(x=10, y=100, width=100, height=20)
        #escrita4
        self.escrita4 = Label(self.janela, text='quantos caracteres(apenas numeros) ? ', anchor=W, background='#d3d3d3')
        self.escrita4.place(x=50, y=140,)
        self.caixadetexto4 = Entry(self.janela)
        self.caixadetexto4.place(x=80, y=160)
        #caixa de texto 2
        self.caixadetexto2 = Entry(self.janela)
        self.caixadetexto2.place(anchor=W, x=55, y=110, width=200, height=20)

        #check button
        self.checkbutton = IntVar()
        self.check = tkinter.Checkbutton(self.janela, text='site permite caracteres especiais ?', variable=self.checkbutton)
        self.check.place(x=10, y=230)

        #botoes
        self.botao1 = self.botoes(self.janela,text='Gerar Senha', anchor=N, comando=self.senhar,x=10, y=270, width=100, height=30)
        self.botao2 = self.botoes(self.janela, text='Salvar Senha', anchor=N, comando=self.combinandofunc, x=10,y=300,width=100, height=30)
        self.botao3 = self.botoes(self.janela, text='mostrar senhas', anchor=N, comando=self.abridor, x=170, y=270, width=100, height=30)
        self.janela.config(background='#d3d3d3')

        #fim da janela
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
        tamanhos = 16
        self.dicionario.clear()
        tm = self.caixadetexto4.get()
        if tm.isnumeric():
            tm = int(tm)
            tamanhos = tm
            print(tm)
            if self.checkbutton.get() == 1:
                chars = string.ascii_letters + string.digits + '!@çÇ#$%&*-_+=?|/¬'
                rng = random.SystemRandom()
                x = ''.join(rng.choice(chars) for i in range(tamanhos))
                self.dicionario.append(x)
                print(x)
                messagebox.showinfo('Senha gerada', f'{x}')
            else:
                chars = string.ascii_letters + string.digits
                rng = random.SystemRandom()
                x = ''.join(rng.choice(chars) for i in range(tamanhos))
                self.dicionario.append(x)
                print(x)
                messagebox.showinfo('Senha gerada', f'{x}')

            pyperclip.copy(x)
        elif tm == '':
            tamanhos = 12
            print(tm)
            if self.checkbutton.get() == 1:
                chars = string.ascii_letters + string.digits + '!@çÇ#$%&*-_+=?|/¬'
                rng = random.SystemRandom()
                x = ''.join(rng.choice(chars) for i in range(tamanhos))
                self.dicionario.append(x)
                print(x)
                messagebox.showinfo('Senha gerada', f'{x}')
            else:
                chars = string.ascii_letters + string.digits
                rng = random.SystemRandom()
                x = ''.join(rng.choice(chars) for i in range(tamanhos))
                self.dicionario.append(x)
                print(x)
                messagebox.showinfo('Senha gerada', f'{x}')

            pyperclip.copy(x)
        else:
            messagebox.showinfo(title='apenas digitos', message='por favor digite a quantidade em forma de digito!')
            self.caixadetexto4.delete(0, END)

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

c = janela(titulo='Gerador.py', lxa='300x400')
