#Bibliotecas
from pytube import YouTube
import moviepy.editor as mp
import re
import os
import tkinter as tk
from tkinter import filedialog
import time

#botão para converter o link em um mp3 e escolher o diretório que deseja salvar
def converter():
    # Abre a caixa de diálogo de seleção de diretório
    link = digitar_link.get()
    path = filedialog.askdirectory()
    
    try:
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download(path)

        # Converter para MP3
        for file in os.listdir(path):
            if file.endswith('.mp4'):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)

        # Exibir mensagem de conclusão
        label_status['text'] = 'Conversão Completa!'
        
    except:
        label_status['text'] = 'Link inválido!'

def limpar_campos():
    digitar_link.delete(0, tk.END)
    label_status['text'] = ''
    
#Interface grafica
janela = tk.Tk()
janela.title('Pytube MP3')

label_conversor = tk.Label(text="Conversor de vídeos do Youtube para MP3", borderwidth=1, relief='solid', fg="white", bg="red")
label_conversor.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_link = tk.Label(text='Insira um link do Youtube: ',  anchor='e')
label_link.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

digitar_link = tk.Entry()
digitar_link.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

button_converter = tk.Button(text='Converter', command=converter)
button_converter.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

button_limpar = tk.Button(text='Limpar', command=limpar_campos)
button_limpar.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

label_status = tk.Label(janela)
label_status.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

janela.mainloop()
