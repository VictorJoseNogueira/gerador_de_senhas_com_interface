import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.title("Example")

# Carrega o GIF usando a biblioteca Pillow
image = Image.open(r"C:\Users\T-GAMER\Desktop\mtrix.gif")
frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(image)]

# Cria um label para exibir o GIF
label = ttk.Label(root, image=frames[0])
label.pack(fill="both", expand="yes")

# Função que é chamada a cada intervalo de tempo para atualizar a imagem
def update_frames(index):
    label.config(image=frames[index])
    root.after(100, update_frames, (index + 1) % len(frames))

root.after(0, update_frames, 0)
root.mainloop()
