#Escribir un programa el nombre del usuario por consola y de paso un número entero; luego debe imprimir el nombre del usuario tantas veces como se le fue indicado en la digitación del número entero.
nombre = input("Ingresa tu nombre: ")
numero = int(input("Ingrese un numero: "))
print("******Forma sencilla*****")
#Forma sencilla
print((nombre + "\n") * numero)
#While
while(numero > 0):
  print(nombre)
  numero -= 1

#Ciclo for
