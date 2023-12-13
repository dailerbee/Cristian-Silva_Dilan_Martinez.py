import random
import math

Max_cod=255
Min_cod=0
Max_vol=12
min_vol=0


N=1000
A=[]
for i in range(N):
    val=random.randint(0,255)
    A.append(val)
    print(i," ", val)


medicion=max(A)
min_medicion=min(A)

A.sort(reverse=False)
medicion=A[-1]
min_medicion=A[0]

print("Max=", medicion)
print("Min=", min_medicion)
b=min_vol
m=Max_vol/Max_cod

voltaje_max=m*medicion+b
voltaje_min=m*min_medicion+b
print("V_Max=", voltaje_max)
print("V_Min=", voltaje_min)

suma=0
for i in range(len(A)):
    suma=suma+A[i]
promedio=suma/len(A)
print("Promedio=", promedio*m+b)

#RMS fomula 1
cuadrados=[]
for i in range(len(A)):
    cuadrados.append(A[i]**2)
suma_cuadrados=0
for i in range(len(A)):
    suma_cuadrados=suma_cuadrados+cuadrados[i]
Vrms=math.sqrt(suma_cuadrados/len(A))
print("Vrms= ", Vrms*m+b)
#RMS 2 formula 2
promediocc=promedio*m+b
vp=promediocc*3.141592
Vrms2=vp/math.sqrt(2)
print("vrms2",Vrms2)
porcenta=Vrms/math.sqrt(Vrms2)
porcentaje_de_error=porcenta
print("porcentaje de error=",porcentaje_de_error)