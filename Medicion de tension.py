import random
import math

Max_cod=255
Min_cod=0
Max_vol=12
min_vol=0


N=10
A=[]
for i in range(N):
    val=random.randint(0,255)
    A.append(val)
    #print(i," ", val)
#print(A)

#max_medicion=max(A)
#min_medicion=min(A)

A.sort(reverse=False)
max_medicion=A[-1]
min_medicion=A[0]

#Tencion maxima
#tension minima
#tension promedio en voltios

B=min_vol
C=Max_vol/Max_cod

voltaje_max=C*max_medicion+B
voltaje_min=C*min_medicion+B
print("V_Max=", voltaje_max)
print("V_Min=", voltaje_min)

#Promedio

suma=0
for i in range(len(A)):
    suma=suma+A[i]
promedio=suma/len(A)
print("Promedio=", promedio*C+B)

#RMS
cuadrados=[]
for i in range(len(A)):
    cuadrados.append(A[i]**2)

suma_cuadrados=0
for i in range(len(A)):
    suma_cuadrados=suma_cuadrados+cuadrados[i]

Vrms=math.sqrt(suma_cuadrados/len(A))
print("Vrms= ", Vrms*C+B)
print(A)