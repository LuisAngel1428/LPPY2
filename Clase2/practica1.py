import random

precio= 10000
print(f"El producto tiene un costo de {precio}")
cantidad=int(input("Cuantos productos va a llevar?\n"))

subtotal=precio*cantidad
porc=0

if subtotal>50000:
    porc=0.05
else:
    porc=0.02

descuento=subtotal*porc
total_a_pagar=subtotal-descuento

if cantidad>0:
    print(f"El porcentaje de descuento es, {porc}")
    print(f"El subtotal a pagar es {subtotal} sin el descuento")
    print(f"El monto del descuento es igual a {descuento}")
    print(f"El monto total a pagar es {total_a_pagar} ya con el descuento aplicado.")
else:
    print("No se pueden vender menos de 1 producto")

