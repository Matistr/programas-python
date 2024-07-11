from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i=0

#entrada
text= Entry(ventana, font=("Calibri 20"))
text.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

#funciones
def click(valor):
    global i
    text.insert(i,valor)
    i+=1

def delete():
    text.delete(0,END)
    i=0
    
def operacion():
    ecuacion=text.get()
    result=eval(ecuacion)
    text.delete(0,END)
    text.insert(0,result)
    i=0
#botones
#boton=Button(ventana,text="",width=5,height=2)
boton1=Button(ventana,text="1",width=5,height=2,command=lambda:click(1))
boton2=Button(ventana,text="2",width=5,height=2,command=lambda:click(2))
boton3=Button(ventana,text="3",width=5,height=2,command=lambda:click(3))
boton4=Button(ventana,text="4",width=5,height=2,command=lambda:click(4))
boton5=Button(ventana,text="5",width=5,height=2,command=lambda:click(5))
boton6=Button(ventana,text="6",width=5,height=2,command=lambda:click(6))
boton7=Button(ventana,text="7",width=5,height=2,command=lambda:click(7))
boton8=Button(ventana,text="8",width=5,height=2,command=lambda:click(8))
boton9=Button(ventana,text="9",width=5,height=2,command=lambda:click(9))
boton0=Button(ventana,text="0",width=13,height=2,command=lambda:click(0))

borrar=Button(ventana,text="AC",width=5,height=2,command=lambda:delete())
boton_par1=Button(ventana,text="(",width=5,height=2,command=lambda:click("("))
boton_par2=Button(ventana,text=")",width=5,height=2,command=lambda:click(")"))
boton_punto=Button(ventana,text=".",width=5,height=2,command=lambda:click("."))

boton_div=Button(ventana,text="/",width=5,height=2,command=lambda:click("/"))
boton_mult=Button(ventana,text="X",width=5,height=2,command=lambda:click("*"))
boton_sum=Button(ventana,text="+",width=5,height=2,command=lambda:click("+"))
boton_resta=Button(ventana,text="-",width=5,height=2,command=lambda:click("-"))
boton_igual=Button(ventana,text="=",width=5,height=2,command=lambda:operacion())

#agregar botones en pantalla
#boton.grid(row=,column=,padx=5,pady=5)
borrar.grid(row=1,column=0,padx=5,pady=5)
boton_par1.grid(row=1,column= 1,padx=5,pady=5)
boton_par2.grid(row=1 ,column=2 ,padx=5,pady=5)
boton_div.grid(row=1,column= 3,padx=5,pady=5)

boton7.grid(row= 2,column=0 ,padx=5,pady=5)
boton8.grid(row= 2,column=1 ,padx=5,pady=5)
boton9.grid(row= 2,column= 2,padx=5,pady=5)
boton_mult.grid(row=2,column=3,padx=5,pady=5)

boton4.grid(row=3,column=0,padx=5,pady=5)
boton5.grid(row=3,column=1,padx=5,pady=5)
boton6.grid(row=3,column=2,padx=5,pady=5)
boton_sum.grid(row=3,column=3,padx=5,pady=5)

boton1.grid(row=4,column=0,padx=5,pady=5)
boton2.grid(row=4,column=1,padx=5,pady=5)
boton3.grid(row=4,column=2,padx=5,pady=5)
boton_resta.grid(row=4,column=3,padx=5,pady=5)

boton0.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
boton_punto.grid(row=5,column=2,padx=5,pady=5)
boton_igual.grid(row=5,column=3,padx=5,pady=5)

ventana.mainloop()