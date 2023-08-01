#valores
mes= input('Indicar mes de nomina: ')
dias_laborales= int(input('Indicar dias laborales: '))
pago_por_dia= float(input('Indicar pago por dia: '))

#procesos
pago_bruto= dias_laborales * pago_por_dia
IVA_trasladado= pago_bruto * 0.16
subtotal= pago_bruto + IVA_trasladado
IVA_retenido= (IVA_trasladado / 3) * 2
ISR_retenido= (pago_bruto * 0.10)
pago_neto= subtotal - IVA_retenido - ISR_retenido


#resultado
print('el pago bruto es: ' ,pago_bruto)
print('el IVA trasladado es: ' ,IVA_trasladado)
print('subtotal =' ,subtotal)
print('IVA retenido =' ,IVA_retenido)
print('ISR retenido =' ,ISR_retenido)
print('pago neto =' ,pago_neto)
