#Como primer paso le pediremos al usaurio qe ingrese la palabra
palabra = input("Ingrese una palabra: ")

#Definiremos un contador
num = 0

#Se revisara la palabra letra por letra
for letra in palabra:
    num += 1

print(f"La palabra {palabra} tiene un total de {num} letras.")   
