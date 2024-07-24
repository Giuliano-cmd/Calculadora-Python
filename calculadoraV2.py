#CalculadoraV2#
import os
import time


#Programa principal#
os.system ("cls")
print("---------------------")
pantalla = str(input(""))
# print("---------------------\n" + pantalla + "\n---------------------")
i = 1
var = pantalla.split()
resultado = int(var[0])
#print (var)
while i < len(var):
    if var[i] == "+":
        resultado = resultado + int(var[i+1])
    elif var[i] == "-":
        resultado = resultado - int(var[i+1])
    else:
        pass
    i = i+1
print("Resultado: " + str(resultado))