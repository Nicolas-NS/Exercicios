from tkinter import *  #importa a biblioteca Tkinter

# criar a janela(TK)
janela = Tk() 

# renomar a janela(title)
janela.title('hello world') 

#informa o tamanho da janela (geometry (X, y))
janela.geometry()

# fazer a janela rodar em loop, (!!precisa ser a ultima linha de codigo pra rodar a janela(mainloop)!!)
#janela.mainloop() 

#--------------------------------------------------------texto-na-janela-----------------------------------------------------------------------

texto1 = Label(janela, text="olá mundo", # colocar um texto  na tela (variavel = label(nome da janela, text='texto na janela")) 
font= ("Arial", 32), # mudar a fonte (fonte= ('fonte', tamanho ))
bg="black",# mudar cor de backgrund (bg= "cor")
fg="blue") # mudar cor de foreground (fg= "cor")

# posicionar o texto na janelan usando (variável.grid(column= coluna, row=linnha)), pensado na tela como uma matriz
texto1.grid(column=0, row=0)

#---------------------------------------------------------Botão-na-janela-------------------------------------------------------------------
#crie uma função:
# (variável.config) Permite manipular as propriadades de uma "widget(botões, label..)"

def ola():
    texto1.config(text="FALA MUNDO!!")


# colocar um botão na tela (variavel = bu(nome da janela, text='texto na janela"))
#obs: as funcões "bg" e "fg"

butão1 = Button(janela, text="clique aqui", bg=('purple'), 
width=('26'), #muda o tamanho do botão (winth='tamanho' (x))
height=('1'), #muda o tamanho do botão (heigth='tamanho' (y))
command=ola) #dar uma  função para o botão (comand= nome da função)

# posicionar o butão
butão1.grid(column=0, row= 2)

#-1-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=--=-=-=-=-=-=-=-=-=-=-=-==-=-PLACE-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# usado para colocar a widget em qual quer lugar da janela usando um referencial de (X e Y)

# butão2 = Button(janela, text="usando place", )
# butão2.place( x=30, y=30,
# height= 25, width= 100, # height, width - Altura e largura em pixels.
# relheight= 0.0, relwidth= 0.0, # relheight, relwidth - Altura e largura como uma flutuação entre 0,0 e 1,0, como uma fração da altura e largura do widget pai.
# relx=0.1, rely=0.5)  # relx rely - deslocamento horizontal e vertical como uma flutuação entre 0,0

#-2-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=--=-=-=-=-=-=-=-=-=-=-=-==-=-GRID-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# usado para o widget na janelan usando como referencia uma matriz na tela

texto1 = Label(janela, text="tudo bem?", font= ("Arial", 32), bg="black", fg="blue")

texto1.grid(column=0, #  column,  a coluna do widget
ipadx=0, # Quantos pixels devem conter o widget, horizontal e verticalmente, dentro das bordas do widget. ipadx = x
ipady=0, # Quantos pixels devem conter o widget, horizontal e verticalmente, dentro das bordas do widget. ipady = y
padx= 0,# Quantos pixels devem conter o widget, horizontal e verticalmente, dentro das bordas do widget.  padx = x
pady= 0,# Quantos pixels devem conter o widget, horizontal e verticalmente, dentro das bordas do widget.  pady = y
row=3 # row, a linha do widget 
)

#---------------------------------------------------------caixa-de-entrada-----------------------------------------------------------------

#entry usado pra colocar uma caixa de entrada na janela e tem as mmesmas configurações de um button
entrada = Entry(janela, width=10, bg="purple")
entrada.grid(column=0, row=5)
#(variavel.get()) para recerber o valor do entry.

def tudobem ():
    n = entrada.get()  
    
    if n == "não":
        texto3 =  Label(janela, text="pq?")
        texto3.grid(column=0, row= 8)
        pq = Entry(janela, width=10 )
        pq.grid(column= 0, row=9)
   
    elif n == 'sim':
        d = Label(janela, text= "A") 
        d.grid(column=0, row=7)

butão3 = Button(janela, text="sim ou não?", command=tudobem)
butão3.grid(column=0, row=6)

sim_não = Label(janela, text="")
sim_não.grid(column=0, row=7)

#---------------------------------------------------------caixa-de-entrada-----------------------------------------------------------------

# fazer a janela rodar em loop, (!!precisa ser a ultima linha de codigo pra rodar a janela(mainloop)!!)
janela.mainloop() 