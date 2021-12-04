# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:20:44 2021

@author: socce
"""
import tkinter as tk
from tkinter import *

ventana = tk.Tk() 
ventana.title("Primera Ventana") #Cambiar el nombre de la ventana 
ventana.geometry("820x8000") #Configurar tamaño 
#Barra de desplazamiento
scroll_bar = Scrollbar(ventana)
scroll_bar.pack( side = 'right',
                fill = 'y' )
    
mylist = Listbox(ventana, 
                 yscrollcommand = scroll_bar.set )


class regla:
    def __init__(self, lectura, escritura, movimiento, estadoDestino):
        self.lectura = str(lectura)
        self.escritura = str(escritura)
        self.movimiento = movimiento
        self.estadoDestino = estadoDestino
        
class estado:
    def __init__(self, name):
        self.name = name
        self.reglas=[]
        self.numeroRegla=[]
        
    def agregarRegla(self, lectura, escritura, movimiento, estadoDestino):
        regla1 = regla(lectura, escritura, movimiento, estadoDestino)
        self.reglas.append(regla1)
        self.numeroRegla.append(lectura)
        
    def movimiento(self, cinta, indice):
        print(cinta, "||||||||",self.name)
        
        numeroDeregla = self.numeroRegla.index(cinta[indice])
        regla = self.reglas.__getitem__(numeroDeregla)
        
        if regla.lectura == cinta[indice]:
            cinta[indice] = regla.escritura
        
        cinta[indice] = regla.escritura

        if regla.movimiento == "R":
            if indice+1 > len(cinta)-1:
                cinta.append(" ")
                indice = indice+1
            else:
                indice = indice+1
           
        elif regla.movimiento == "L":
            if indice-1 < 0:
                cinta.insert(0," ")
                indice = 0
            else:
                indice = indice-1
                
        elif regla.movimiento == "S":
            indice = indice
        
        if regla.estadoDestino != 0:
            print(cinta)
            mylist.insert(END, cinta)
            regla.estadoDestino.movimiento(cinta,indice)
        else:
            mylist.insert(END, "\n\n")
            print("CINTA DE SALIDA:",cinta)

def main(entrada):    
    
    cintaInput=list(entrada.get())
    estados=[]

    if len(cintaInput) == 0:
        print(Exception("La entrada esta vacia"))
    else:
        print("CINTA DE ENTRADA:",cintaInput,"\n")
        for i in range(0,17):
            q0 = estado(i)
            estados.append(q0)
    
    #REGLAS ESTADO 0
    estados[0].agregarRegla('A','A','R',estados[1])
    estados[0].agregarRegla('B','B','R',estados[1])
    estados[0].agregarRegla('C','C','R',estados[1])
    
    #REGLAS ESTADO 1
    estados[1].agregarRegla('A','A','R',estados[1])
    estados[1].agregarRegla('B','B','R',estados[1])
    estados[1].agregarRegla('C','C','R',estados[1])
    estados[1].agregarRegla(' ','Y','L',estados[2])
    
    #REGLAS ESTADO 2
    estados[2].agregarRegla('A','A','L',estados[2])
    estados[2].agregarRegla('B','B','L',estados[2])
    estados[2].agregarRegla('C','C','L',estados[2])
    estados[2].agregarRegla(' ',' ','R',estados[3])
    
    #REGLAS ESTADO 3    
    estados[3].agregarRegla('A','A','R',estados[4])
    estados[3].agregarRegla('B','B','R',estados[4])
    estados[3].agregarRegla('C','C','R',estados[4])
    
    #REGLAS ESTADO 4
    estados[4].agregarRegla('A','X','R',estados[5])
    estados[4].agregarRegla('B','X','R',estados[6])
    estados[4].agregarRegla('C','X','R',estados[7])
    estados[4].agregarRegla('Y','Y','L',estados[11])
    
    #REGLAS ESTADO 5
    estados[5].agregarRegla('A','A','R',estados[5])
    estados[5].agregarRegla('B','B','R',estados[5])
    estados[5].agregarRegla('C','C','R',estados[5])
    estados[5].agregarRegla('Y','Y','R',estados[5])
    estados[5].agregarRegla(' ','A','L',estados[8]) 
    
    #REGLAS ESTADO 6
    estados[6].agregarRegla('A','A','R',estados[6])
    estados[6].agregarRegla('B','B','R',estados[6])
    estados[6].agregarRegla('C','C','R',estados[6])
    estados[6].agregarRegla('Y','Y','R',estados[6])
    estados[6].agregarRegla(' ','B','L',estados[9]) 
    
    #REGLAS ESTADO 7
    estados[7].agregarRegla('A','A','R',estados[7])
    estados[7].agregarRegla('B','B','R',estados[7])
    estados[7].agregarRegla('C','C','R',estados[7])
    estados[7].agregarRegla('Y','Y','R',estados[7])
    estados[7].agregarRegla(' ','C','L',estados[10]) 
    
    #REGLAS ESTADO 8
    estados[8].agregarRegla('A','A','L',estados[8])
    estados[8].agregarRegla('B','B','L',estados[8])
    estados[8].agregarRegla('C','C','L',estados[8])
    estados[8].agregarRegla('Y','Y','L',estados[8])
    estados[8].agregarRegla('X','A','R',estados[4]) 
    
    #REGLAS ESTADO 9
    estados[9].agregarRegla('A','A','L',estados[9])
    estados[9].agregarRegla('B','B','L',estados[9])
    estados[9].agregarRegla('C','C','L',estados[9])
    estados[9].agregarRegla('Y','Y','L',estados[9])
    estados[9].agregarRegla('X','B','R',estados[4])
    
    #REGLAS ESTADO 10
    estados[10].agregarRegla('A','A','L',estados[10])
    estados[10].agregarRegla('B','B','L',estados[10])
    estados[10].agregarRegla('C','C','L',estados[10])
    estados[10].agregarRegla('Y','Y','L',estados[10])
    estados[10].agregarRegla('X','C','R',estados[4])
    
    #REGLAS ESTADO 11
    estados[11].agregarRegla('A','A','L',estados[11])
    estados[11].agregarRegla('B','B','L',estados[11])
    estados[11].agregarRegla('C','C','L',estados[11])
    estados[11].agregarRegla(' ',' ','R',estados[12])
    
    #REGLAS ESTADO 12
    estados[12].agregarRegla('A','A','R',estados[13])
    estados[12].agregarRegla('B','B','R',estados[14])
    estados[12].agregarRegla('C','C','R',estados[15])

    #REGLAS ESTADO 13
    estados[13].agregarRegla('A','A','R',estados[13])
    estados[13].agregarRegla('B','B','R',estados[13])
    estados[13].agregarRegla('C','C','R',estados[13])
    estados[13].agregarRegla('Y','A','R',estados[16])
    
    #REGLAS ESTADO 14
    estados[14].agregarRegla('A','A','R',estados[14])
    estados[14].agregarRegla('B','B','R',estados[14])
    estados[14].agregarRegla('C','C','R',estados[14])
    estados[14].agregarRegla('Y','B','R',estados[16])
    
    #REGLAS ESTADO 15
    estados[15].agregarRegla('A','A','R',estados[15])
    estados[15].agregarRegla('B','B','R',estados[15])
    estados[15].agregarRegla('C','C','R',estados[15])
    estados[15].agregarRegla('Y','C','R',estados[16])
    
    #REGLAS ESTADO 16
    estados[16].agregarRegla('A','A','R',estados[16])
    estados[16].agregarRegla('B','B','R',estados[16])
    estados[16].agregarRegla('C','C','R',estados[16])
    estados[16].agregarRegla(' ',' ','S',0)
    
    #INICIO DE LAS TRANCISIONES
    estados[0].movimiento(cintaInput, 0)

def interfaz():
    #Titulo    
    etiqueta = tk.Label(ventana, text = "Maquina de PhyTuring")
    etiqueta.pack()
    
    #caja de Texto
    entrada = tk.Entry(ventana)
    entrada.pack()
    
   
    #Boton iniciar
    boton = tk.Button(ventana, text = "Iniciar", padx=50, pady=5, command = lambda: main(entrada))
    boton.pack()
    
    mylist.pack(fill = BOTH, ipadx=50, ipady=800 )  
    scroll_bar.config( command = mylist.yview )
    ventana.mainloop()
  
interfaz()







        
        