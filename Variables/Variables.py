"""
~~ Practicando variables en Python ~~
~~ Ángel Torada ~~
"""

#~~ Visibilidad ~~
    #Todas las variables definidas fuera de una función son globales
#~~Tipos~~
    #int, float, str y bool
#Son Case sensitive X != x
#Se pueden definir de nuevo  x = 1 -> x = 2
x = 1
y = 2.2
texto = "Hola" #Es lo mismo que texto = 'Hola' 
boolean = True #O False

#Pruebas
    #Output int
print(type(x))
    #Output float
print(type(y))
    #Output str
print(type(texto))
    #Output bool
print(type(boolean))

#Se pueden definir más de una variable a la vez
    #Diferente contenido
orange, banana, cherry = "Orange", "Banana", "Cherry"
print(orange)
print(banana)
print(cherry)
    #Mismo contenido
orange = banana = cherry = "Igual"
print(orange)
print(banana)
print(cherry)



#~~ Colecciones ~~


    #Diccionarios (Unordered y con Key-Values)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
    #Output Muestra todo
print(thisdict)
    #Output Longitud del diccionario
print(len(thisdict))
    #Output Muestra solo el modelo
print(thisdict["model"]) # thisdict.get("model") Es lo mismo
    #Podemos obtener sus Keys con thisdict.keys()
print(thisdict.keys())
    #Podemos obtener sus valores con thisdict.values()
print(thisdict.values())
    #Devuelve cada key-value en forma de tuplas en una lista
print(thisdict.items())
    #Se puede comprobar si una key existe en un diccionario con
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
    #Añadir un solo dato
thisdict["color"] = "red" # thisdict.update({"color": "red"}) es lo mismo
    #Modificar solo un dato
thisdict["year"] = 2018 # thisdict.update({"year": 2020}) es lo mismo
    #Eliminar un solo dato
thisdict.pop("model") #thisdict.popitem() Elimina el último
                      #del thisdict["model"] Elimina uno en específico
                      #del thisdict Elimina todo el diccionario
#Recorrer un diccionario
    #Solo las Keys
for x in thisdict: #thisdict.keys() es lo mismo
  print(x)
    #Solo los datos
for x in thisdict: #thisdict.values() es lo mismo
  print(thisdict[x])
    #Ambos
for x, y in thisdict.items():
  print(x, y)
#Para copiar un diccionario podemos usar el método thisdict.copy() o dist(thisdict)
#Se pueden crear diccionarios anidados





    #Listas (Se pueden repetir valores, ordered y changeable) Pueden tener diferentes tipos de datos
mylist = ["apple", "banana", "cherry"]
#Saber su tamaño
print(len(mylist))
#Acceder a su primer item, a su último o a X rango
print(mylist[0])
print(mylist[-1])
print(mylist[1:3]) #Primero incluido, último no.
print(mylist[2:]) #Del segundo al último

#Saber si un dato está dentro de la lista
if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")
  
#Modificar el contenido de un elemento 
mylist[1] = "blackcurrant"
#Modificar el contenido de varios elementos
mylist[1:3] = ["blackcurrant", "watermelon"] #El último no cuenta y si insertamos uno de más los de después se moverán uno a la derecha
#Insertar un dato
mylist.insert(2, "watermelon") #En una posición específica
mylist.append("orange") #Al final
#Para juntar dos listas usamos mylist.extend(thislist) No tiene porqué ser otra lista

#Eliminar de una lista
# Te pide una lista, no un elemento -> mylist.remove("banana") #Borra todos los elementos parecidos
mylist.pop(1) #Elimina solo el primer elemento, sino ponemos un parámetro borrará el último dato
#También se puede hacer con del mylist[0]

#Maneras de reccorer una lista
for x in mylist:
  print(x)
  
for x in range(len(mylist)):
  print(mylist[x])
  
[print(x) for x in mylist]

#Para ordenarla 
mylist.sort() #.sort(reverse = True) para realizar el inverso
#Juntar dos listas 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
#También funciona
#for x in list2:
  #list1.append(x)
  
#Para copiarla 
thislist = mylist.copy() #list(mylist) es lo mismo
#Para limpiarla
mylist.clear()
#Para eliminar a una vista podemos usar
del mylist





    #Sets (Unordered, unchangeable [Pudiendo añadir nuevos valores], sin duplicados y permiten tener diferentes tipos dentro)
thisset = {"apple", "banana", "cherry"}
print(thisset)

#No se puede acceder a ellos como en las colecciones anteriores, hay que recorrerlos con un Loop
for x in thisset:
  print(x)
#Sí permite comprobar si existe cierto valor detro
print("banana" in thisset)
#Para añadir contenido al set
thisset.add("orange")
#Para juntar dos Sets
#Se puede usar el método union para juntar ambos sets y devolver uno nuevo set3 = set1.union(set2)
#Si solo queremos los duplicados de ambos, lo podremos conseguir con set1.intersection_update(set2)
#Si solo queremos los duplicados y en un nuevo Set usaremos set3 = set1.intersection(set2)
#Sus contrapartes, es decir, solo los no duplicados serían:
#set1.symmetric_difference_update(set2) y set3 = set1.symmetric_difference(set2)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Para eliminar un elemento podemos usar remove o discard
thisset.discard("banana") # thisset.remove("banana")
#Borrar el último elemento
x = thisset.pop()
#Borrar todo en el Set
thisset.clear()    
#Borrar el Set
del thisset




    #Tuplas (Ordenada, Unchangeable [Sin añadir nuevos valores], permite duplicados y permite tener varios tipos a la vez)
thistuple = ("apple", "banana", "cherry") #Si queremos crearla con solo un valor habría que dejar la coma Final
print(thistuple)
#Para saber la Longitud
print(len(thistuple))
#Para acceder a alguno de sus valores podemos usar 
print(thistuple[1]) #También admite el índice negativo (para ir al último o vice), rangos EJ: 2:5. (Siempre incluye el primero pero nunca el último)
#Para comprobar que un valor existe en la tupla
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#La única manera de añadir o eliminar elementos es haciendole un casting a lista y posteriormente a tupla de nuevo || list()
#Sumar dos tuplas sin embargo sí se puede 
y = ("orange",)
thistuple += y
print(thistuple)
#Otra manera sería
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
#Se puede duplicar el contenido de las tuplas con un *
mytuple = thistuple * 2
#Borrar una tupla
del thistuple
#Se pueden "descomprimir" los datos de las tuplas en variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
#Si hay más de un valor restante en la tupla podemos añadir * a alguna de las variables para que meta los datos como lista
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits