#Pediremos un numero al usuario
num = input("Ingrese un numero: ")

contador = 0

for digitos in num:
    contador += 1

print(f"La cantidad de digitos que tiene el numero {num} es de {contador}.") 