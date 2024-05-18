#nombre, tipo y cantidad

print("Tipo     Precio")
print("A        ->80")
print("B        ->105")
print("C        ->250")
print("Que modelo desea llevar?")
tipo=input().upper()
cant=int(input("Cuantas unidades desea llevar?\n"))
precio=0 #valor inicial de precio
if tipo=="A":
    precio=80
    print(f"El precio del modelo {tipo} es {precio}")
elif tipo=="B":
    precio=105
    print(f"El precio del modelo {tipo} es {precio}")
elif tipo=="C":
    precio=250
    print(f"El precio del modelo {tipo} es {precio}")
else:
    print("El modelo ingresado no es valido")



total=precio*cant

if cant==0:
    print("La cantidad a llevar no puede ser 0")
elif cant<0:
    print("No puede ser un numero negativo")
else:
    print(f"El total a pagar es {total}")

#solicitar cantidad de pantalones
#calcular el total a pagar
#condicionar las salidas para que se muestre solo si la cantidad es postitiva