#valores 
celcius= 8.99
farenheit= 10.30
kelvin= 2.15



#procesos
kelvin_celcius= round(kelvin - 273.15)
kelvin_farenheit= round((9 * (kelvin - 273.15))/5 + 32)
farenheit_celcius= round((5 * (farenheit - 32))/9)
farenheit_kelvin= round((5 * (farenheit - 32))/9 + 273.15)
celcius_kelvin= round(celcius + 273.15)
celcius_farenheit= round((9 * celcius)/5 + 32)




#resultados
print(kelvin_celcius)
print(kelvin_farenheit)
print(farenheit_celcius)
print(farenheit_kelvin)
print(celcius_farenheit)
print(celcius_kelvin)
