#Calculadora#
import os
import time


#Programa principal#
def menuprinc():
	os.system ("cls")
	print("---------------------")
	print("[S] - Suma")
	print("[R]- Resta")
	print("[D]- División")
	print("[M]- Multiplicación")
	print("[O]- Salir")
	print("---------------------")
	global opc
	opc = str(input("Indique operacion: "))
	while opc != "S" and opc != "s" and opc != "R" and opc != "r" and opc != "M" and opc != "m" and opc != "d" and opc != "D" and opc != "o" and opc != "O":
		os.system ("cls")
		print("---------------------")
		print("[S] - Suma")
		print("[R]- Resta")
		print("[D]- División")
		print("[M]- Multiplicación")
		print("[O]- Salir")
		print("---------------------")
		opc = str(input("Por favor, ingrese un dato valido: "))
	if opc == "S" or opc == "s":
		suma()
	elif opc == "R" or opc == "r":
		resta()
	elif opc == "m" or opc == "M":
		multiplicacion()
	elif opc == "d" or opc == "D":
		division()
	else:
		salir()



#Funciones de las operaciones#
#Funcion suma#
def suma():
	num1 = int and float(input("Ingrese primer numero: "))
	num2 = int and float(input("Ingrese segundo numero: "))
	suma = num1 + num2
	print("Su suma es: ", suma)
	time.sleep(0.50)
	continuar()

#Funcion resta#
def resta():
	num1 = int and float(input("Ingrese primer numero: "))
	num2 = int and float(input("Ingrese segundo numero: "))
	resta = int (num1 - num2)
	print("Su resta es: ", resta)
	time.sleep(0.50)
	continuar()

#Funcion multiplicacion#
def multiplicacion():
	num1 = int and float(input("Ingrese primer numero: "))
	num2 = int and float(input("Ingrese segundo numero: "))
	mult = num1 * num2
	print("Su multiplicación es: ", mult)
	time.sleep(0.50)
	continuar()

#Funcion division#
def division():
	num1 = int and float(input("Ingrese primer numero: "))
	num2 = int and float(input("Ingrese segundo numero: "))
	div = num1 / num2
	print("Su division es: ", div)
	time.sleep(0.50)
	continuar()

#Funcion salir#
def salir():
	os.system ("cls")
	print("Saliendo del programa.")
	time.sleep(0.70)
	os.system ("cls")
	print("Saliendo del programa..")
	time.sleep(0.70)
	os.system ("cls")
	print("Saliendo del programa...")
	time.sleep(0.50)

#Funcion continuar operando#
def continuar():
	seguir = str(input("Continuar "))

#Ciclo menu#
menuprinc()
while opc != "o" and opc != "O":
	menuprinc()