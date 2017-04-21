# -*- coding: utf-8 -*-
'''
@author: d16raruf
'''

from pCalculadora2.op_bas import *

while True:
    print """
-------------MENU CALCULADORA---------------
 
Pulse 1 para sumar dos dígitos
Pulse 2 para restar dos dígito
Pulse 3 para multiplicar dos dígitos
Pulse 4 para dividir dos dígitos 
Pulse 5 para salir del progama
"""
    
    opcion=input("Que número desea: ")
    
    if opcion == 1:
        print sumar(a=input("Introduzca el primer numero: "), b=input("Introduzca el segundo numero: "))
    elif opcion == 2:
        print restar(a=input("Introduzca el primer numero: "), b=input("Introduzca el segundo numero: "))
 
    elif opcion == 3:
        print multiplicar(a=input("Introduzca el primer numero: "), b=input("Introduzca el segundo numero: "))
 
    elif opcion == 4:
        print dividir(a=input("Introduzca el primer numero: "), b=input("Introduzca el segundo numero: "))
        
    elif opcion == 5:
        print "Hasta luego"
        break
 
    else:
        print "\nOpción incorrecta. Introduzca un número válido"
        
