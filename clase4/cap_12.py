print(f"""
Talla   Precio
S       50
M       55
L       60
XL      65
XXL     70""")
print("Seleccione la talla")
talla=input("Ingrese la talla\n").upper()
cantidad=int(input("Cuantas desea comprar\n"))
precio=0

match talla:
    case "S":
        precio=50
    case "M":
        precio=55
    case "L":
        precio=60
    case "XL":
        precio=65
    case "XXL":
        precio=70
    case _:
        print("La talla es invalida")

porc=0
if cantidad>6 and cantidad<12:
    porc=0.05
elif cantidad>12 and cantidad<24:
    porc=0.10
elif cantidad>24:
    porc=0.15

subtotal=cantidad*precio
monto_desc=subtotal*porc
total=subtotal-monto_desc

talla_valida=(talla=="S" or talla=="M" or talla=="L" or talla=="XL" or talla=="XXL")

if cantidad>=0:
    print(f"""
        Talla: {talla}
        Precio {precio}
        Cantidad: {cantidad}
        Subtotal: {subtotal}
        Descuento: {porc*100}%
        Monto descuento; {monto_desc}
        Total: {total}""")
else:
    print("La cantidad no puede ser 0 ni numero negativo.")
if not talla_valida:
    print("No se puede procesar la venta")
    print("Ha ingresado datos invalidos")