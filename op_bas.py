#! -*- coding: UTF-8 -*-
'''
a) Cree un módulo llamado op_bas.py con las siguientes funciones: 
sumar, restar, multiplicar, dividir.
Cada función recibirá dos parámetros (los operandos). Cada función devolverá el resultado de la operación. 
Controle la excepción de la división por cero en la función dividir.

b) Documente el módulo y las funciones con las siguientes cadenas de texto:
Modulo --> Módulo Op_bas.
sumar --> Función que suma los dos parametros y devuelve el resultado.
restar --> Función que resta los dos parametros y devuelve el resultado.
multiplicar --> Función que multiplica los parámetros y delvuelve el resultado.
dividir --> Función que divide los parámetros (numerador, denominador) y devuelve el resultado.

c)  Crea un módulo nuevo : 
A continuación importa el módulo del ejercicio anterior en el siguiente código, 
de forma que las instrucciones siguientes se ejecuten sin producir errores:

a, b = 13, 3
print 'Operandos =', a, b
print 'sumar = ', op_bas.sumar (a, b)
print 'restar = ', op_bas.restar (a, b)
print 'multiplicar = ', op_bas.multiplicar (a, b)
print 'dividir = ', op_bas.dividir (a, b)

d) Crea un módulo nuevo:  
A continuación importa el módulo del ejercicio anterior en el siguiente código,
de forma que las instrucciones siguientes se ejecuten sin producir errores:
a, b = 13, 0
print 'Operandos =', a, b
print 'sumar = ', sumar (a, b)
print 'restar = ', restar (a, b)
print 'multiplicar = ', multiplicar (a, b)
print 'dividir = ', dividir (a, b)

Todo los módulos anteriores en un paquete . 
e) Crear un módulo fuera del paquete, que permita mostrar un menú en pantalla, 
para permitir al usuario seleccionar la opción de la pCalculadora. 
   Calculadora 
   Seleccione opción: 
         1. Sumar. 
         2. Restar 
         3. Multiplicar 
         4. Dividir 
         0. Salir 
         OPción: .....
         
@author: Francisco Ramírez
'''

def sumar (a, b):
    """Función que suma los dos parametros y devuelve el resultado."""
    return a + b

def restar (a, b):
    """Función que resta los dos parametros y devuelve el resultado."""
    return "resultado",a - b

def multiplicar (a, b):
    """Función que multiplica los parámetros y delvuelve el resultado."""
    return a * b

def dividir (a, b):
    """Función que divide los parámetros (numerador, denominador) y devuelve el resultado."""
    try:
        resultado = a / b
    except ZeroDivisionError:
        print 'ERROR: No se puede dividir por cero'
        return ""
    return resultado