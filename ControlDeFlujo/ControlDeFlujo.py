"""
~~ Practicando Control de Flujo en Python~~
~~ Ángel Torada ~~
"""


#En Python hay 3 tipos de control de flujo básicos, vamos a verlos

#If - Else
#En este se establece un condicional, si se cumple entra en el if, sino en el else 
#También existe el elif que es un condicional extra en caso de que el primer if no se cumpla

#Los principales condicionales son 
# == (Igual), != (Diferente), < (Menor que), > (Mayor que), <= (Menor o igual que), >= (Mayor o igual que)

a = 2
b = 1

#Es importante tener espaciados
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")

#Se pueden hacer if's en una sola línea
if a > b: print("a es mayor que b")
 #También se pueden hacer con else
print("A") if a > b else print("B")

#Se pueden hacer Ifs anidados
x = 40
if x > 10:
  print("Es mayor que 10")
  if x > 20:
    print("También es mayor que 20")
  else:
    print("Pero no mayor que 20")
    

#También está permitido el uso de y's (and) y o's (or)
    #And
a = 2
b = 1
c = 3
if a > b and c > a:
  print("Las dos condiciones se cumplen") 
    #Or
if a > b or a > c:
  print("Una de las dos condiciones se ha cumplido")
  
#Al igual que las funciones los IFs no pueden estar vacíos, pero podemos usar la palabra pass para evitar un error de compilación
if b > a:
  pass






#Bucles While
#Los bucles while son bucles que se repiten hasta que la condición deje de ser true, es por esto que hay que tener cuidado e intentar que acaben
#Se pueden realizar bucles anidados

i = 1 #Variable contador
while i < 6:
  i += 1 #Contador que incrementa la variable para que acabe en algún momento el bucle
  
#Los Whiles tienen tres sentencias relevantes a tener en cuenta: Continue, Break y Else

#Break se encarga de terminar el bucle por completo
    #Cuando la variable contador llegue a 3 el bucle se cortará
i = 1
while i < 6:
  print(i)
  if i == 3:
    print("Entra en el break")
    break
  i += 1
  
#Continue se encarga de terminar la iteración actual y pasar a la siguiente

i = 0
while i < 6:
  i += 1
  if i == 3:
    print("Entra en el if")
    continue
  #Si incrementasemos la variable contador aquí como en los casos anteriores al llegar al número 3 dejaría de incrementarse por el continue y sería un bucle infinito
  print(i)
  
    #Else se encarga de realizar una sentencia final una vez el bucle while deje de ser true

i = 1
while i < 6:
  i += 1
else:
  print("El bucle ha terminado")

#Al igual que en las Funciones y en los IF's un While no se puede dejar vacío, es por esto que se puede utilizar pass para evitarlo.
#Igualmente, realizar esto implica que la condición NUNCA acabaría por lo que no tendría mucho sentido hacerlo




#Bucles For Loop
#Los bucles For Loop son aquellos que se encargan de recorrer un rango (Este rango pueden ser números, los elementos de una coleccion o los carácteres de una cadena de texto)
#Se pueden realizar For Loops anidados

    #Recorriendo una lista
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

    #Recorriendo una cadena
for x in "banana":
  print(x)
  
    #También se puede usar la sentencia break como en el caso anterior 

for x in fruits:
  print(x)
  if x == "banana":
    break

    #Al igual que el uso del break está permitido el del continue también

for x in fruits:
  if x == "banana":
    continue
  print(x)
  
    #En caso de que queramos hacerlo sobre un rango tendremos que usar la sentencia range con el número máximo de iteraciones
for x in range(6):
  print(x)
    #También podemos forzar a que empiece por un número en concreto en vez de por 0
for x in range(2, 6):
  print(x)
    #También podemos cambiar el incremento para que deje de ser de uno en uno a que sea de 3 en 3 (O whatever)
for x in range(2, 30, 3):
  print(x)
    
    #Else también está permitido en los For Loops como podemos ver en el siguiente ejemplo
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("El bucle ha acabado")
  

#Al igual que en los IF's y las Funciones los For Loops no se pueden dejar vacíos, es por esto que usamos Pass
for x in [0, 1, 2]:
  pass

