#valores 
calificacion_1= 5.56
calificacion_2= 8.15
calificacion_3= 9.36
calificacion_4= 3.25
calificacion_5= 10.0





#procesos
suma_1= calificacion_1 + calificacion_2 + calificacion_3 + calificacion_4 + calificacion_5
suma_2= calificacion_1 + calificacion_4 
suma_3= calificacion_2 + calificacion_4 + calificacion_5
promedio_1= round(suma_1 / 5)
promedio_2= round(suma_2 / 2)
promedio_3= round(suma_3 / 3)



#resultados 
print('el promedio es =' ,promedio_1) 
print('el promedio es =' ,promedio_2) 
print('el promedio es =' ,promedio_3)






#Valores 
promedio_alpha= float(input("Ingresa el promedio: "))


#Procesos 
if (promedio_alpha > 6 and promedio_alpha < 10):
    print("APROVADO")
elif (promedio_alpha == 6):
    print("PANSASO")
elif (promedio_alpha > 0 and promedio_alpha < 6):
    print("REPROBADO")
elif (promedio_alpha < 0 or promedio_alpha > 10):
    print("PROMEDIO INVALIDO")















