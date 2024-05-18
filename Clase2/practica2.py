print("Cuantos dolares va a comprar?")
cant=int(input())
print("Tenemos disponible  Tasa BCV (1) y tasa Paralelo (2), cual prefieres?")
print("La tasa por defecto es Paypal")
opcion=int(input())
tasa_bcv=36.58
tasa_par=39.51
tasa_paypal=37
tasa=0

if opcion==1:
    tasa=tasa_bcv

if opcion==2:
    tasa=tasa_par

total=cant*tasa

print(f"El costo segun la tasa seleccionada es {tasa}")
print(f"El total a pagar es {total}")