#Aquí he puesto algunos ejercicios (No muy complejos) para practicar Control de flujo, Operadores, Inputs, Librerias(Modulo built-in)
#https://www.discoduroderoer.es/ejercicios-propuestos-y-resueltos-basicos-en-python/

#1
print("Hola mundo")

#2
x,y=1,1
print(x+y)

#3
valor = 100
print("IVA: " + str(100*0.21))
print("Total: " + str((100*0.21) + 100))

#4
num1=1
num2=2
print(num1) if(num1 > num2) else print(num2)

#5
entre=5
if (entre>0 and entre<10): print("Está entre 0 y 10")

#6
if (entre>21 and entre<30): 
    print("Está entre 21 y 30")
elif (entre>11 and entre<20): 
    print("Está entre 11 y 20")
elif (entre>0 and entre<10): 
    print("Está entre 0 y 10")

#7
contador=1
while contador <= 100:
    print(contador)
    contador+=1

#8
for i in range(1,101):
    print(i)

#9
for i in "Hola Mundo":
    print(i)

#10
for i in range(1,101):
    if(i%2 == 0):
        print(i)

#11
rango = list(range(10))
print(rango)

#12 (Solución aportada por la página)
rango = list(range(5,10))
print(rango)
#Solución para solo 1 número como dice el ejercicio
import random
n = random.randint(5,10) 
print(n)

#13
rango = list(range(10,-1,-1))
print(rango)

#14
rango1 = list(range(0,11))
rango2 = list(range(10,21))
print(rango1)
print(rango2)

#15
rango = list(range(0,len("Hola Mundo")))
print(rango)

#16
cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")
print(cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:])

#17
cadena1 = input("Palíndromo: ")
alreves = cadena1[::-1]
if( cadena1 == alreves ):
    print("Es palindromo")
else:
    print("No es palindromo")

#18
import random
numero=random.randint(1,100) 
intento=1
while (True):
    print("Intento " + str(intento))
    numerousuario=int(input("Introduzca el número: "))
    if(numerousuario == numero):
        print("Has ganado")
        break
    elif(numerousuario<numero):
        print("El número introducido es menor")
    else:
        print("El número introducido es mayor")
    intento += 1


#Probando clases y funciones

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def haAprobado(self):
        if(int(self.nota)>=5):
            print("Ha aprobado")
        else:
            print("No ha aprobado")

a1 = Alumno("Ángel","1")
a2 = Alumno("Ángel","10")
print(a1.nombre)
print(a2.nota)
a2.nota=5
print(a2.nota)
a1.haAprobado()
a2.haAprobado()

from abc import ABC,abstractmethod
class A():
    def __init__(self, nombre):
        self.nombre = nombre
    @abstractmethod
    def saludar(self):
        print("Saludar")

class B(A):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    def saludar(self):
        print("Hola " + self.nombre)

b = B("Ángel","Rojo")
b.saludar()
