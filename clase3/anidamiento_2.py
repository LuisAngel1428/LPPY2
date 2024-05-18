
edad=int(input("Ingresa tu edad\n"))
estudiante=input("Eres estudiante? si/no \n").upper()
precio=10
porc=0
if edad>0:
    if edad<2:
        porc=1
    elif edad<=5:
        porc=0.5
    elif edad<=10:
        porc=0.2
    elif edad>=55:
        porc=0.3

if estudiante=="SI":
    if porc<0.25:
        porc=0.25

monto_desc=precio*porc
total_pagar=precio-monto_desc

if porc>0:
    print(f"""Porcentaje de descuento {porc*100}%
                El monto de descuento es igual a {monto_desc}
                El total a pagar es de {total_pagar}""")