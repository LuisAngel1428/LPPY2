nombre=input("Como te llamas?\n")
edad=int(input("Cuantos años tienes?\n"))
estado_civil=input("Ingresa tu estado civil (S)oltero (C)asado (P)areja\n").upper()

mayor_edad=(edad>=18)
soltero=(estado_civil=="S")
casado=(estado_civil=="C")
pareja=(estado_civil=="P")

if mayor_edad:
    print(f"{nombre} es MAYOR de edad")
else:
    print(f"{nombre} es MENOR de edad")
#not

if not mayor_edad:
    print(f"{nombre} es MENOR de edad")
else:
    print(f"{nombre} es MAYOR de edad")

if not soltero:
    print(f"{nombre} no esta soltero")
    if not casado:
        print(f"{nombre} no esta casado")
    else:
        print(f"{nombre} esta casado")
    if not pareja:
        print(f"{nombre} no tiene pareja")
    else:
        print(f"{nombre} tiene pareja")
else:
    print(f"{nombre} esta soltero")

