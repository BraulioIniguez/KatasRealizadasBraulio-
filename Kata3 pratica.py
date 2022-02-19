# Tip de práctica 1: Intenta ejecutarlo en un notebook.
from asyncio import StreamReaderProtocol
from re import S

a = 40
b = 55
# test expression / expresión de prueba
if a < b:
    # statement to be run / instrucción a ejecutar
    print(str(b)+" verdadero")
    
#*******************************************

# Aplica el tip de práctica 2.
a = 93
b = 27
if a >= b:
    print(str(a) + " verdadero")
    #**************************************

a = 24
b = 44
if a <= 0:
    print(a)
print(str(b)+ " Es falso") #Este ejemplo no lo comprendi del todo.

#/**************************************************

a = 93
b = 27
if a >= b:
    print(str(a) + " es verdadero")
else:
    print(str(b) + " es falso ")

#******************   Implementacion de if, Else y elif  ***
print(str("********  verdadera    **********************************"))
print(str("Implementacion de if, Else y elif "))

a = 93
b = 27
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else: 
    print ("a es igual que b")

#*********************  Ahora si fuera falsa  **************
print(str(""))
print(str("Ahora la sentencia falsa"))
a = 20
b = 27
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b a<b")
else: 
    print ("a es igual que b")
#**************************************************
print(str("*******************************"))
print(str(" Operaciones or"))
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)
#******************************************
print(str(" ***************************"))
print(str(" operador and"))
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)
    

