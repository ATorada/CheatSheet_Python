"""
~~ Practicando Librerías en Python~~
~~ Ángel Torada ~~
"""



#~~ Módulos locales y Built-In ~~

#Las librerías son (usualmente) aquel cojunto de módulos con código externo (Métodos, variables...) Que podemos llamar con un Import 

#Lo más sencillo son los módulos. Los módulos son aquellas clases sencillas con código y que podemos llamar y usar de la siguiente manera 
#También existen módulos Built-In (Que no hay que descargar) que podemos usar (https://docs.python.org/3/py-modindex.html)

import Modulo #También se puede importar el Módulo con un alias  [import Modulo as mod], para usar su contenido con mod. podríamos hacerlo
#El import del módulo se puede hacer con el sistema de paquetes, es decir, si el módulo B está dentro de la carpeta A, podremos hacer import A.B
#Al igual que se puede hacer con paquetes, se puede usar con rutas relativas: from .(actual) import echo, from ..(Una atrás) import echo, from ..codigo(atrás en codigo) import echo 
#Método del Módulo sin parámetros
Modulo.gato()
#Método del Módulo CON parámetros
Modulo.saludar("Ángel")
#Acceso a una colección en el Módulo
print("Años: " + str(Modulo.queso["años"]) + " Tipo: " + Modulo.queso["tipo"] + " Tamaño: " + Modulo.queso["tamaño"])

#La sentencia dir([nombre_modulo]), nos permite conocer todos los métodos y variables de un módulo
print(dir(Modulo))


#~~ Librerías externas ~~

#Por último también podemos importar solo métodos/variables de un módulo de la siguiente manera -> from Modulo import queso 
#Para usar queso NO deberemos hacer referencia al módulo como antes X -> Modulo.queso["año"] ✔ -> queso["año"]

#Sin embargo una librería es un cojunto de módulos, veamos el uso de una
#Para empezar al no ser Built-in  hay que instalarla, yo voy a hacer una prueba con NumPy
#Para instalar la librería pondré en una consola el siguiente comando "pip install numpy"
#Importante destacar que si no tenemos un entorno virtual tendremos que hacerlo sobre la consola del ordenador
#Acto seguido haremos el import
import numpy as np #Usaremos un alias sobre la librería de la siguiente manera

#Ahora vamos a usarla creando un sencillo Array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#Y lo mostramos
print(a[0])