#La manera de definir funciones es con: def [Nombre de la funcion]():
#No se pueden crear funciones sin código, para que esto sea posible pondremos el statement pass dentro de la función para que no quede vacía 
def Hola_Mundo():
    print("Hola mundo")

#Para llamarla usaremos
Hola_Mundo()

#La manera de definir funciones CON ARGUMENTOS es con: def [Nombre de la funcion](argumento1, argumento2):
#Los parámetros siempre serán aceptados independientemente de lo que sea, tendremos que ser nosotros quienes lo filtren
def Hola_Nombre(nombre):
    print("Hola "+ nombre)

Hola_Nombre("Ángel")

#Si se exceden pasando argumentos podremos usar el prefijo * sobre el parámetro y acceder a él como una TUPLA
def Hola_Nombres(*nombres):
  print("Hola, en específico, a: " + nombres[2])

Hola_Nombres("Ángel", "Cristian", "Iván")

#Si usamos varios argumentos, a la hora de llamar a la Función podremos especificar cada uno (Keywords or Kwargs)
def Hola_Nombres_Especificos(nombre1, nombre2, nombre3):
  print("Hola, en específico, a: " + nombre2)

Hola_Nombres_Especificos(nombre3 = "Ángel", nombre2 = "Cristian", nombre1 = "Iván")

#Si no sabemos la cantidad de Keywords que nos pasarán podremos especificar cual queremos mostrar con **. (Como un diccionario)
def Hola_MuchosNombres(**Nombres):
    print("Hola, en específico, a: " + Nombres["nombre1"])
    
Hola_MuchosNombres(nombre1="Ángel", nombre2="Cristian")

#Si llaman a la función SIN parámetro podremos establecer uno por defecto con =
def Hola_Nombre(nombre = "David"):
    print("Hola "+ nombre)

Hola_Nombre("Ángel")
Hola_Nombre()

#Para crear una función que retorne algo tendremos que usar return
def suma(val1):
    return val1 + 2

print(suma(2))



#Recursividad 
#La recursividad es un tema complejo, pero podemos pensar que es un bucle, tiene un condicional que implica el fin, sino, se repite.
#En este ejemplo he pensado en un Gato que quiere comer, nosotros sabemos que el gato está a 10 pasos de su comida
#Si hicieramos un bucle le diríamos que se repitiera 10 veces el caminar hasta que llegase a su comida
#Sin embargo, con recursividad simplemente crearíamos la funcion VaAComer que se llamaría a sí misma hasta que se hubieran restado los 10 pasos
#Para ello definimos 0 como "Ha llegado a comer" y en caso de que no sea 0 entonces siempre restaremos un paso.
def VaAComer(Distancia):
  if(Distancia > 0):
    VaAComer(Distancia - 1)
  else:
      print("Ha llegado a su comida")

VaAComer(10)



#Lambda 
#Las Lambda son funciones anónimas que solo aceptan una expresión, pero es una manera sencilla de realizar una función en una línea
#Por ejemplo, queremos crear una función de suma, para crearla usaríamos la plantilla [Nombre de la funcion] = lambda [Argumentos] : [Expresion]
sumaLambda = lambda a, b : a + b
print(sumaLambda(2,2))
#Se les llama anónimas, porque principalmente se usan sin nombre dentro de otra función, como en el siguiente ejemplo

#Establecemos una función base que retorna una función lambda en la que se establece el valor base según el parámetro pasado por la función
def multiplicacionBase(base):
  return lambda num : num * base

#Creamos dos funciones lambda que tienen como número base 2 y 3 respectivamente
doblador = multiplicacionBase(2)
triplicador = multiplicacionBase(3)

#Llamamos a las lambda con su parámetro(num)
print(doblador(11))
print(triplicador(11))
 