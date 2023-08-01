# valores
agua= float(input('Ingresa el nivel de agua: '))

#Evento (procesos)
if (agua > 6 ):
    print('DESBORDAMIENTO DE AGUA EN CISTERNA')
elif (agua == 6):
    print('APAGAR BOMBA')
elif (agua > 4 and agua < 6 ):
    print('DESACELERAR BOMBA')
elif (agua > 2 and agua < 4):
    print('BOMBA TRABAJANDO')
elif (agua > 0 and agua < 2):
    print('ACELERAR BOMBA DE AGUA')
elif (agua == 0):
    print('ENCENDER LA BOMA DE AGUA')
elif (agua < 0):
    print('FUGA EN CISTERNA')
    
