from email.mime import image
from tkinter import*
from PIL import Image, ImageTk
# importando speedteste
import speedtest

co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#3fb5a3"
co3 = "#fc766d"
co4 = "#403d3d"
co5 = "#4a88e8"

# Criando a janela
janela = Tk()
janela.title("Internet Speed Test")
largura = 350
altura = 200
janela.resizable(width=FALSE, height=FALSE)
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
posX = largura_screen/2 - largura/2
posY = altura_screen/2 - altura/2
janela.geometry("%dx%d+%d+%d" % (largura, altura,posX,posY))
janela.configure(background=co1)

# Dividindo Janela em 2 frames
frame_logo = Frame(janela, width=largura, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=largura, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando o frame_logo
imagem = Image.open('speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)
l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=20, y=0)
l_logo_nome = Label(frame_logo, text='Internet Speed Test', compound=LEFT, padx=10, anchor=NE, font=('Ivy 16 bold italic'), bg=co1, fg=co4)
l_logo_nome.place(x=75, y=15)

l_logo_linha = Label(frame_logo,width=largura, anchor=NW, font=('Ivy 1'), bg=co2)
l_logo_linha.place(x=0, y=57)

# função de teste
def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"
    l_download['text'] = download
    l_upload['text'] = upload
    botao_testar['text'] = 'Teste novamente'
    botao_testar.place(x=115,y=100)

    
# configurando frame_corpo
l_download = Label(frame_corpo, text="",anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_download.place(x=44, y=25)
l_download_Mbps = Label(frame_corpo, text="Mbps download",anchor=NW, font=('Ivy 10 italic'), bg=co1, fg=co4)
l_download_Mbps.place(x=30, y=70)
imagem_down = Image.open('down.png')
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)
l_logo_imagem_down = Label(frame_corpo, height=60, image=imagem_down, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem_down.place(x=140, y=35)

l_upload = Label(frame_corpo, text="",anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_upload.place(x=235, y=25)
l_upload_Mbps = Label(frame_corpo, text="Mbps upload",anchor=NW, font=('Ivy 10 italic'), bg=co1, fg=co4)
l_upload_Mbps.place(x=230, y=70)
imagem_up = Image.open('up.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)
l_logo_imagem_up = Label(frame_corpo, height=60, image=imagem_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem_up.place(x=175, y=35)

botao_testar = Button(frame_corpo,command=main, text="Iniciar Teste",font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1)
botao_testar.place(x=125, y=100)

janela.mainloop()
