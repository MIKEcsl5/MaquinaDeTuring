# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:20:44 2021

@author: socce
"""

alfabeto=["a",'b','c']
entrada="AB"
cintaInput=list(entrada)
cintaInput.append(" ")
cintaInput.insert(0, " ")
estados=[]

class regla:
    def __init__(self, lectura, escritura, movimiento, estadoDestino):
        self.lectura = str(lectura)
        self.escritura = str(escritura)
        self.movimiento = movimiento
        self.estadoDestino = estadoDestino
        
class estado:
    def __init__(self):
        self.reglas=[]
        self.numeroRegla=[]
        
    def agregarRegla(self, lectura, escritura, movimiento, estadoDestino):
        regla1 = regla(lectura, escritura, movimiento, estadoDestino)
        self.reglas.append(regla1)
        self.numeroRegla.append(lectura)
        
    def movimiento(self, cinta, indice):
        numeroDeregla = self.numeroRegla.index(cinta[indice])
        regla = self.reglas.__getitem__(numeroDeregla)
        
        if regla.lectura == cinta[indice]:
            cinta[indice] = regla.escritura
        
        cinta[indice] = regla.escritura

        if regla.movimiento == "R":
            if indice+1 > len(cinta):
                cinta.append(" ")
                indice = indice+1
            else:
                indice = indice+1
           
        elif regla.movimiento == "L":
            if indice-1 < 0:
                cinta.insert(0," ")
                indice = indice-1
            else:
                indice = indice-1
                
        elif regla.movimiento == "S":
            indice = indice
        
        if regla.estadoDestino != 0:
            print(cinta)
            regla.estadoDestino.movimiento(cinta,indice)
        else:
            print("CINTA DE SALIDA:",cinta)

def main(cintaInput):    
    if len(cintaInput) == 0:
        print(Exception("La entrada esta vacia"))
    else:
        print("CINTA DE ENTRADA:",cintaInput,"\n")
        for i in range(0,18):
            q0 = estado()
            estados.append(q0)
    
    #REGLAS ESTADO 0
    estados[0].agregarRegla('A','A','R',estados[1])
    estados[0].agregarRegla('B','B','R',estados[1])
    estados[0].agregarRegla('C','C','R',estados[1])
    
    #REGLAS ESTADO 1
    estados[1].agregarRegla('A','A','A',estados[1])
    estados[1].agregarRegla('B','B','R',estados[1])
    estados[1].agregarRegla('C','C','R',estados[1])
    estados[1].agregarRegla(' ','Y','L',estados[1])
    
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
    estados[5].agregarRegla('A','A','R',estados[8])
    estados[5].agregarRegla('B','B','R',estados[8])
    estados[5].agregarRegla('C','C','R',estados[8])
    estados[5].agregarRegla('Y','Y','R',estados[8])
    estados[5].agregarRegla(' ','A','L',estados[8]) 
    
    #REGLAS ESTADO 6
    estados[6].agregarRegla('A','A','R',estados[9])
    estados[6].agregarRegla('B','B','R',estados[9])
    estados[6].agregarRegla('C','C','R',estados[9])
    estados[6].agregarRegla('Y','Y','R',estados[9])
    estados[6].agregarRegla(' ','B','L',estados[9]) 
    
    #INICIO DE LAS TRANCISIONES
    estados[0].movimiento(cintaInput, 0)

main(cintaInput)






        
        