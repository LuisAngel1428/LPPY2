ventas=float(input("Cuanto vendio en el mes?\n"))
edad=int(input("Cual es su edad?\n"))
sexo=input("Ingrese sexo F/M\n").upper
sbase=500
porc=0
bono=0

if ventas>0 and ventas<75000:
    porc=0.05
elif ventas>=90000 and ventas<200000:
    porc=0.07
elif ventas>=300000 and ventas<1000000:
    porc=0.08
elif ventas>=1500000:
    porc=0.10
else:
    porc=0.06

if (edad>=55 and sexo=="F") or (edad>=60 and sexo=="M"):
    bono=40000

comision=ventas*porc
salariof=sbase+comision

if bono>0:
    print("Ha recibido el bono de la tercera edad")
print(f"El porcentaje de comision obtenido es {porc*100}%")
print(f"""La comision por ventas es {comision}
            El salario final es {salariof}""")    