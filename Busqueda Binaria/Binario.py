
import time

def busquedaBinaria(lista, item):
  if len(lista) == 0:
    return False
  else:
    medio = len(lista)//2
    if lista[medio] == item:
      print("El número: " + str(item) + " se encontro en la posición: " + str(lista[medio]))
      return True
    else:
      if item < int(lista[medio]):
        return busquedaBinaria(lista[:medio], item)
      else:
        return busquedaBinaria(lista[medio+1:], item)


def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)): # Este ciclo for, recorre la lista en un rango desde 1 hasta la longitud.
    # La variable "valorActual", sirve como varible temporal, para saber que dato tenemos en esa posicion.
     valorActual = unaLista[indice]
     posicion = indice
    # El siguiente ciclo while se utiliza para insertar los valores, con ayuda de un operador lógico, denominado, 
    # "and", para que cumpla ambas condiciones y se pueda ordenar la lista.
     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual


Arr = [1,3,5,6,7,9,10,2,4,8,12,14,16,18,19,20,11,13,15,17]

print("Arreglo no ordenado")
print(Arr)
ordenamientoPorInsercion(Arr)
print("Arreglo Ordenado")
print(Arr)

var = int(input("Cual de los elementos del arreglo desea Buscar --> "))

hms = time.time()

busquedaBinaria(Arr, var)
print((time.time()) - hms)


