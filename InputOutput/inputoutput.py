#El Input en python es bastante sencillo, hay dos maneras de realizarlo
#raw_input() o input(). Depende de la versión funcionará uno u otro. El Raw se usa en la 2.7 y el Input en la 3.6 (De normal)

frase = input("¡Di algo!")
print(frase)

#En mi versión no funciona el Raw_input
#frase = raw_input("¡Di algo!")
#print(frase)


#Igualmente esto es para la introducción de datos por consola ¿Qué pasa si queremos leer y escribir un archivo?
#Para ello usaremos la sentencia open() en esta se incluirá el archivo y el modo (r para leer, a para append, w para escribir y x para crear)
#También se puede indicar si será tratado como binario(b) o como texto(t) [Por defecto]

f = open("C:\\Users\\Sabiin\\Desktop\\PythonRepaso\\InputOutput\\archivo.txt", "rt") #Sin ningún parámetro lo abriremos solo de lectura
print(f.read())

#También podemos poner la cantidad de carácteres que queremos leer  (En caso de que ya lo hayamos leído este parámetro no funcionará)
print(f.read(3))

#En caso de que tenga más de una línea podremos ir leyendo una por una con la sentencia readline
#Lee solo la primera
print(f.readline())
#Se guarda en el buffer que la primera ha sido leída y lee la segunda
print(f.readline())

#También se puede leer con un bucle de la siguiente manera
for x in f:
  print(x)


#Después de haber abierto un archivo es MUY IMPORTANTE cerrarlo, para ello simplemente pondremos la siguiente línea
f.close()


#Para escribir en un archivo tendremos que indicar que vamos a hacerlo, para ello lo añadiremos al final del texto ya existente o reescribiremos el texto ya contenido
#a - Append mantiene lo anterior y w - Write sobreescribe lo anterior

#Append
f = open("C:\\Users\\Sabiin\\Desktop\\PythonRepaso\\InputOutput\\archivo.txt", "a")
f.write("Una línea más")
f.close()

#Sobreescribimos
f = open("C:\\Users\\Sabiin\\Desktop\\PythonRepaso\\InputOutput\\archivo.txt", "w")
f.write("Lo he borrado todo :(")
f.close()


#En caso de que queramos crear un nuevo archivo usaremos la siguiente sintaxis
#Lo crea vacío
f = open("nuevoarchivo.txt", "x")
f.close()
#Lo crea pero podremos escribir directamente en el programa
f = open("nuevoarchivo.txt", "w")
f.close()


#Por último también podremos borrar archivos y carpetas, para ello usaremos la librería os
import os
os.remove("nuevoarchivo.txt")

if os.path.exists("archivoquenoexiste.txt"):
  os.remove("archivoquenoexiste.txt")
else:
  print("El archivo no existe")

#Permite borrar una carpeta  
os.rmdir("carpetaABorrar")