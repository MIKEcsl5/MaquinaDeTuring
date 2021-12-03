# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:20:44 2021

@author: socce
"""

alfabeto=["a",'b','c']
entrada="AB"
cintaInput=list(entrada)
#cintaInput.append(" ")
#cintaInput.insert(0, " ")




if len(cintaInput) == 0:
    print(Exception("La entrada esta vacia"))

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
        self.estadosDestino=[]
        
    def agregarRegla(self, lectura, escritura, movimiento, estadoDestino):
        regla1 = regla(lectura, escritura, movimiento, estadoDestino)
        self.reglas.append(regla1)
        self.numeroRegla.append(lectura)
        self.estadosDestino = estadoDestino
        
    def movimiento(self, cinta, indice):
        numeroDeregla = self.numeroRegla.index(cinta[indice])
        regla = self.reglas.__getitem__(numeroDeregla)
        print(numeroDeregla)
        
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
        
        print(indice, cinta)
        regla.estadoDestino.movimiento(cinta,indice)

q0=estado()
q1=estado()
q2=estado()
q3=estado()
q4=estado()
q5=estado()
q6=estado()
q7=estado()
q8=estado()
q9=estado()
q10=estado()
q11=estado()
q12=estado()
q13=estado()
q14=estado()
q15=estado()
q16=estado()
q17=estado()

q0.agregarRegla('C','C','R',q1)
q0.agregarRegla('A','YY','R',q1)
q1.agregarRegla('B','zzz','R',q1)

q0.movimiento(cintaInput, 0)
print(cintaInput)


"""

    def agregarDestinos(self, estadosDestino):
        self.estadosDestino = estadosDestino
        
q0.agregarDestinos([q1])
q1.agregarDestinos([q1,q2])
q2.agregarDestinos([q2,q3])
q3.agregarDestinos([q4])
q4.agregarDestinos([q5,q7,q11])
q5.agregarDestinos([q5,q8])
q6.agregarDestinos([q6,q9])
q7.agregarDestinos([q7,q10])
q8.agregarDestinos([q4,q8])
q9.agregarDestinos([q4,q9])
q10.agregarDestinos([q4,q10])
q11.agregarDestinos([q11,q12])
q12.agregarDestinos([q13,q14,q15])
q13.agregarDestinos([q13,q16])
q14.agregarDestinos([q14,q16])
q15.agregarDestinos([q15,q16])
q16.agregarDestinos(q16,q17)


"""



        
        