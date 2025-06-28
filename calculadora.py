import tkinter
from tkinter import *
from tkinter import ttk


#cores
cor1= "#010c14"
cor2= '#ffffff'
cor3= "#1a1c46"
cor4= '#676b85'
cor5= '#c2410a'


janela= Tk()
janela.title('Calculadora')
janela.geometry('270x400')
janela.config(bg=cor1)

frame_tela= Frame(janela, width=270, height=70, bg=cor3 )
frame_tela.grid(row=0, column=0)

frame_corpo= Frame(janela, width=270, height=330 )
frame_corpo.grid(row=1, column=0)

#armazenar todas expreções que serão usadas
tdsvalores= ""
valortxt= StringVar()

#criando função dos botões
def entrarvalor(event):
    global tdsvalores
    tdsvalores= tdsvalores+str(event)
    valortxt.set(tdsvalores)

def calcular():
    global tdsvalores
    resultado= eval(tdsvalores)
    print(resultado)

def limpar_tela():
    global tdsvalores
    tdsvalores= ""
    valortxt.set("")


#criar label(ação dos botoões)
app_label= Label(frame_tela, textvariable=valortxt, width=20, height=3, padx=7, relief=FLAT, justify=RIGHT, font=('Ivy 20 bold'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#criando botões
b1= Button(frame_corpo, command=limpar_tela, text='C', width=14, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b1.place(x=0, y=0)
b2= Button(frame_corpo,command=lambda:entrarvalor('%'), text='%', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b2.place(x=130, y=0)
b3= Button(frame_corpo, command = lambda: entrarvalor('/'), text='/', width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED)
b3.place(x=195, y=0)
b4= Button(frame_corpo, command = lambda: entrarvalor('7'), text='7', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b4.place(x=0, y=66)
b5= Button(frame_corpo, command = lambda: entrarvalor('8'), text='8', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b5.place(x=65, y=66)
b6= Button(frame_corpo, command = lambda: entrarvalor('9'), text='9', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b6.place(x=130, y=66)
b7= Button(frame_corpo, command = lambda: entrarvalor('*'), text='*', width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED)
b7.place(x=195, y=66)
b8= Button(frame_corpo, command = lambda: entrarvalor('4'), text='4', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b8.place(x=0, y=132)
b9= Button(frame_corpo, command = lambda: entrarvalor('5'), text='5', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b9.place(x=65, y=132)
b10= Button(frame_corpo, command = lambda: entrarvalor('6'), text='6', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b10.place(x=130, y=132)
b11= Button(frame_corpo, command = lambda: entrarvalor('-'), text='-', width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED)
b11.place(x=195, y=132)
b12= Button(frame_corpo, command = lambda: entrarvalor('1'), text='1', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b12.place(x=0, y=198)
b13= Button(frame_corpo, command = lambda: entrarvalor('2'), text='2', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b13.place(x=65, y=198)
b14= Button(frame_corpo, command = lambda: entrarvalor('3'), text='3', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b14.place(x=130, y=198)
b15= Button(frame_corpo, command = lambda: entrarvalor('+'), text='+', width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED)
b15.place(x=195, y=198)
b16= Button(frame_corpo, command = lambda: entrarvalor('0'), text='0', width=14, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b16.place(x=0, y=264)
b17= Button(frame_corpo, command = lambda: entrarvalor('.'), text='.', width=7, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED)
b17.place(x=130, y=264)
b18= Button(frame_corpo,command= calcular, text='=', width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED)
b18.place(x=195, y=264)



janela.mainloop()


