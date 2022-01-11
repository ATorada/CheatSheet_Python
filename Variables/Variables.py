"""
~~ Practicando variables en Python~~
~~ Ángel Torada ~~
"""

#~~Visibilidad~~
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

#Colecciones
    #Diccionarios (Unordered y con Key-Values)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
    #Output Muestra todo
print(thisdict)
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

