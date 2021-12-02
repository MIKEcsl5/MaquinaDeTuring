# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:20:44 2021

@author: socce
"""

alfabeto=["a",'b','c']
entrada="abcb"
cintaInput=list(entrada)
cintaInput.append(" ")
cintaInput.insert(0, " ")



if len(cintaInput) == 0:
    print(Exception("La entrada esta vacia"))

class regla:
    def __init__(self, lectura, escritura, movimiento):
        self.lectura = lectura
        self.escritura = escritura
        self.movimiento = movimiento
        
class estado:
    def __init__(self):
        self.reglas=[]
        self.numeroRegla=[]
        self.estadosDestino=[]
        
    def agregarRegla(self, lectura, escritura, movimiento):
        regla1 = regla(lectura, escritura, movimiento)
        self.reglas.append(regla1)
        self.numeroRegla.append(lectura)
        
    def movimiento(self, cinta, indice):
        numeroDeregla = self.numeroRegla.index(cinta[indice])
        regla = self.reglas.__getitem__(numeroDeregla)
    
    def agregarDestinos(self, estadosDestino):
        self.estadosDestino = estadosDestino

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


q0.agregarDestinos([q1])
q1.agregarDestinos([q1,q2])






        
        