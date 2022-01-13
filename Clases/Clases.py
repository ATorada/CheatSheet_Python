#La manera de definir clases en Python es con: class [Nombre de la clase]:
class Globo:
    #Para defininir su constructor se usa __init__ y como mínimo el parámetro self (Se refiere a la instancia del objeto)
    #Para llamar a un atributo de la instancia usamos self.[Nombre del atributo]
    #El parámetro self se puede nombrar al gusto, pero es OBLIGATORIO
    #También es posible aplicar un valor por default igual que en las funciones al poner atributo = "valor" (Ejemplo con color) 
    #Los que no tienen valores por defecto DEBEN ir antes que los que SÍ tienen
    def __init__(self,flota,color="Verde"):
        self.color = color
        self.flota = flota
    #Para definir una función usamos def [Nombre de la función]([Self],(...)):
    def estaFlotando(self):
        if(self.flota):
            print("Está flotando")
        else:
            print("No está flotando")
    def mostrarColor(self):
        print(self.color)
        
    #Hay maneras de ReDefinir el ToString de las clases con los métodos __str__ o __rept__
    def __str__(self):
        return "Soy un globo de color " + self.color
            
#Para instanciar un objeto usarmos la siguiente estructura
globo = Globo(True, "Rojo")
#Para llamar al ToString usaremos la siguiente estructura
print(str(globo))
#Para llamar a un método usaremos la siguiente estructura
globo.estaFlotando()

#Para obtener el valor de un atributo podremos usar
print(globo.color)

#Para cambiar el valor de un atributo podremos usar 
globo.flota = False
globo.estaFlotando()

#Para eliminar un valor de un atributo podremos usar
del globo.color
globo.mostrarColor

#Si queremos borrar la instancia usaremos el statement del
del globo

#La herencia en clases, es sencilla de entender, simplemente tendremos que establecer como parámetro cuando definimos la clase, a la clase padre
class GloboDeFiesta(Globo):
    #Podemos usar super() o [Nombre de la clase padre].__init__ para llamar al constructor padre y usarlo en el constructor de nuestro objeto hijo
    def __init__(self, color, Flota, tieneLuces):
        super().__init__(Flota, color) #Globo.__init__(self, color, Flota), si utilizamos el nombre de la clase habrá que introducir self, super lo omite
        #Podremos establecer otros atributos propios de la clase hijo
        self.tieneLuces = tieneLuces
    
    def Luces(self):
        if(self.tieneLuces):
            print("Soy un globo de fiesta con luces :D")
        else:
            print("Soy un globo de fiesta sin luces :(")
            
globoFiesta = GloboDeFiesta("Azul",False,True)
globoFiesta.Luces()
globoFiesta.mostrarColor()

#También existe la herencia múltiple de clases, para ello simplemente pondremos las diferentes clases de las que hereda en los () que acompañan al nombre de la clase

#Aquí tenemos un claro ejemplo de como se tratarían los atributos de las diferentes clases de las que hereda
class Animal:                   
   def __init__(self, patas): 
      self.patas = patas 
  
class Alimentacion:
    def __init__(self, tipo):
        self.tipo = tipo

class Gato(Animal, Alimentacion):         
   def __init__(self, patas, tipo, comidaFav): 
      self.comidaFav = comidaFav
      #Sería de caracter obligatorio el poner la clase seguida del __init__ el uso de super() haría que la compilación diese problemas
      Animal.__init__(self,patas)
      Alimentacion.__init__(self, tipo) 
      print("Patas: {}, Tipo de Alimentación: {},Comida Favorita: {}".format(self.patas, self.tipo ,self.comidaFav))

Gato1 = Gato('4','Carnívoros','Pescado')


#Ejemplo con métodos

#En este ejemplo la clase4 hereda de la clase2 y clase3 y estas a su vez de la clase 1
#Todas tienen el método m y en él se hace un print a parte de llamar a al método m de la clase de la que heredan
#Es por esto que el output mostará un print por cada clase de la herencia múltiple. Primero de la principal 4, luego de la 3 y la 2 y por último de la 1 (La base)
#Como vemos aunque tanto la clase2 como la clase3 hereden de la clase1 en el output solo saldrá un In Class1 en vez de 2 (Uno por el super de la clase 2 y otro por el de la clase3)
# (Esto es porque Python sabe que ambas heredan de la clase1 y suprime uno de los dos prints)

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

#Es importante el orden en el que hereda las clases, si fuera Clase2 y Clase3 el output de los métodos sería -> 4-2-3-1 en vez de 4-3-2-1
class Class4(Class3, Class2):
    def m(self):
        print("In Class4")  
        super().m()

obj = Class4()
obj.m()

#También hay una manera de mostrar de qué clases hereda una clase
print(Class4.mro()) #Devolverá una lista
print(Class4.__mro__) #Devolverá una tupla

#Como información extra es posible redefinir los setters, getters y deletters de las clases con el decorator @property, abajo hay un ejemplo

class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        #Getter
        print("Se llama al getter")
        return self._x

    @x.setter
    def x(self, value):
        print("Se llama al setter")
        self._x = value

    @x.deleter
    def x(self):
        print("Se llama al deletter")
        del self._x

c = C()
print(c.x)
c.x = 1
del c.x
