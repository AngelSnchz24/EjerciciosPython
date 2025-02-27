#Encontrar el primer multiplo de 7 mayor que 100
#definimos
num = 101

#Si no es multiplo de 7 aumentara
while num % 7 !=0:
    num += 1

#Imprimimos el resultado
print("El primer numero multiplo de 7 que es mayor que 100 es:", num)