#Primero vamosa pedir el numero al usuario
num = int(input("Ingrese un numero: "))

#Luego para imprimir la tabla de multiplicar usaremos el siguiente comando0
print(f"La tabla de multiplicar de el numero {num} es: ")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")