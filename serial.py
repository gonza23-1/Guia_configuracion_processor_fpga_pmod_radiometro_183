# -*- coding: utf-8 -*-
#el codigo puede presentar un error al correr, relacionado con la conversion de string a float
#para solucionarlo solo correr el progrmaa de nuevo. 
#otros de los probelmas que puede presentar son; 
#1.- Problema al cargar el paquete serial. En particular esto sucede usando anaconda en window10
#2.- Problemas con la conexion serial, esta depende netamente del puerto y el ritmo de envio de datos (baud rate)
#   el problema que se presenta aqui, se debe a que al correr el codigo nuevamente se trata de crear 2 veces la misma conexion
#   para evitar eso es necesario luego de la primera ejecucion descomentar #data.close() ya que esto corta la comunicacion 
#   con el puerto y permitiendo volver a crearla en cualquier momento. 
#autor: Gonzalo Burgos 
# CePIA, udec
#Consultas a Gonza2486@gmail.com 


import serial                         #libreria para comunicacion serial 
from time import time                 #libreria para registrar el tiempo
import numpy as np                    #libreria para manejo de arreglos
from matplotlib import pyplot as plt  #libreria para plotear graficos

N_muestras= 10000                               #se define el numero de muestras 
#en caso de tener problemas con la conexion del puerto serial, descomentar la siguiente linea de codigo
#data.close()

data= serial.Serial('Com4',115200);             #se crea el objeto que define la conexion serial, 'com4' puerto de conxion, baud

#arreglo para datos y variables de control
datos=[]
x=[]
i=0

timepo_inicial_00=time()                        #toma el timepo inical en segundos
while i<N_muestras:
    if (float(data.readline())>2.50):
        print("jeje")
    else:
        datos.append((float(data.readline())))
        #el codigo comentado entrega el tiempo que demora tomar cada dato, no es necesario utilizarlo
#        tiempo_inicial = tiempo_final
#        tiempo_final = time()
#        tiempo_de_toma_de_datos = tiempo_final-tiempo_inicial
#        print("tiempo de ejecucion",tiempo_de_toma_de_datos) 
    i +=1

timpo_final_00=time()                           #toma de tiempo final 
tiempo_total=(timpo_final_00-timepo_inicial_00) #calcula el tiempo de ejecucion del codigo


data.close()                                    #termina la comunicacion serial
dataplot = np.asarray(datos)                    #redimensiona el arreglo para plotearlo

#se guardan los datos en un archivo.txt
header = "data"
np.savetxt("pseudo_8_s_10000.txt",dataplot, header=header )


#Se plotean los datos
plt.title('10000 muestras (pseudo), 8 pines conectados al setup ')
plt.xlabel("Muestra")
plt.ylabel("Volts")
plt.plot(dataplot, "o")
plt.savefig('pseudo_8_s_10000.pdf') #guardando figura
plt.show()
data.close()

  
print("tiempo de ejecucion",tiempo_total)           #imprimime el tiempo de ejecucion de la toma de datos 
print("promedio por dato", tiempo_total/N_muestras) #imprimime el tiempo promedio por dato
