import random
from tkinter import *
from tkinter import messagebox
import os

c = os.path.dirname(__file__)
nome_do_arquivo = c + '\\gerador.txt'

dicio = []


def senhar():
    lista = ['!', '@', '#', '$', '%', '&', '*']
    listaa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'o', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    senha = []

    u = random.choice(lista)
    d = random.choice(listaa)
    t = random.choice(listaa)
    q = random.choice(listaa)
    c = random.choice(listaa)
    s = random.choice(listaa)
    se = random.randint(0, 9)
    o = random.randint(0, 9)
    senha.append(u)
    senha.append(d)
    senha.append(t)
    senha.append(q)
    senha.append(c)
    senha.append(s)
    var = str(se)
    senha.append(var)
    var1 = str(o)
    senha.append(var1)
    x = ''.join(senha)
    dicio.append(x)
    print(x)


def definirsenha():
    bancodesenha = open(nome_do_arquivo, "a")
    bancodesenha.write('Site: ' + caixadetexto.get() + ' \n')
    bancodesenha.write('Login: ' + caixadetexto2.get() + ' \n')
    bancodesenha.write('Senha: ' + dicio[0])
    bancodesenha.write('\n\n')
    dicio.clear()
    bancodesenha.close()


janelinha = Tk()
janelinha.title('Gerador de Senhas 1.0')
janelinha.geometry('300x200')
linha1 = Label(janelinha, text='gerador de senhas automatico', anchor=W)
linha1.place(x=10, y=10, width=200, height=20)
site = Label(janelinha, text='Site', anchor=W)
site.place(x=10, y=30, width=200, height=20)
caixadetexto = Entry(janelinha)
caixadetexto.place(x=10, y=50, width=100, height=20)
login = Label(janelinha, text='login', anchor=W)
login.place(x=10, y=70, width=200, height=20)
caixadetexto2 = Entry(janelinha)
caixadetexto2.place(x=10, y=90, width=200, height=20)
botao2 = Button(janelinha, text='Salvar', command=definirsenha)
botao2.place(x=10, y=150, width=100, height=20)
butaozinho = Button(janelinha, text='Gerar senha', command=senhar)
butaozinho.place(x=10, y=120, width=100, height=20)

janelinha.mainloop()
