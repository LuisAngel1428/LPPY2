


edad=-1

while edad<=0:
    edad=int(input("Ingresa tu edad\n"))
    if edad<0:
        print("La edad no puede ser negativa")
print()        
print("SEGUNDO WHILE")   

edad=-1
while not edad>0:
    edad=int(input("Ingresa tu edad\n"))
    if edad<0:
        print("La edad no puede ser negativa")