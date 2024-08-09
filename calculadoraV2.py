#CalculadoraV2#
import os
import time


#Programa principal#
os.system ("cls")
print("---------------------")
calculo = str(input(""))
calculo =  calculo + "/"
# print("---------------------\n" + pantalla + "\n---------------------")
i = 0
resultado = 0
numeroTemp = ""
primerNum = False
opeActual = ""
#print (var)
while i < len(calculo):
    if calculo[i].isdecimal():
        numeroTemp = numeroTemp + calculo[i]
        print(numeroTemp)
    if primerNum == False and calculo[i].isdecimal() == False:
        resultado = resultado + int(numeroTemp)
        numeroTemp = ""
        primerNum = True
        opeActual = calculo[i]
    elif primerNum == True and calculo[i].isdecimal() == False:
        if opeActual == "+":
            resultado = resultado + int(numeroTemp)
            numeroTemp = ""
            opeActual = calculo[i]
        elif opeActual == "-":
            resultado = resultado - int(numeroTemp)
            numeroTemp = ""
            opeActual = calculo[i]
        else:
            pass
    i = i+1
print("Resultado: " + str(resultado))