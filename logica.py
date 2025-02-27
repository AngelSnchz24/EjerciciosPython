#Cajero automatico

usuario = list()


usuario.append("Angel Sanchez") #string str
usuario.append("1234")          #string str
usuario.append(1000)            #int

recibo = list()
recibo.append(["123", 600])
recibo.append(["124", 845])
recibo.append(["125", 67])
recibo.append(["126", 500])
recibo.append(["127", 100])
recibo.append(["128", 1000])

acciones = list()
acciones.append("Depositar")
acciones.append("Pago de recibo")
acciones.append("Retirar")

usuario2 = list()
usuario2.append("Jose") #string str
usuario2.append("5678")          #string str
usuario2.append(1500)            #int

def registrar():
    usuarioRegistrado = list()
    usuarioC = input("Ingrese su nombre: ")
    usuarioRegistrado = input("Ingrese su password: ")

    if usuarioC == usuario[0] and usuarioRegistrado == usuario[1]:
            print("Bievenido al cajero automatico.")
    else:
          print("Usuario o password incorrecta.")

    return registrar

#git push -u origin main
#git add
#git commit