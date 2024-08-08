#CalculadoraV2#
import os
import time


#Programa principal#
os.system ("cls")
print("---------------------")
calculo = str(input(""))
# print("---------------------\n" + pantalla + "\n---------------------")
i = 0
resultado = 0
numeroTemp = ""
#print (var)
while i < len(calculo):
    if calculo[i].isdecimal():
        numeroTemp = numeroTemp + calculo[i]
        print(numeroTemp)
    else:
        resultado = resultado + int(numeroTemp)
        numeroTemp = ""
    i = i+1
print("Resultado: " + str(resultado))