#valoreS
numero= int(input('Ingrese el nuemro: '))
j=0

#procesos
if (numero < 0 and numero > -100):
    for i in range(-1, -100, -2):
        print(i)

elif (numero > 0 and numero < 100):
    while(j < 100):
        print(j)
        j = j + 2

else:
    print('No valido')






















