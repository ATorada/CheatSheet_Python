#La manera de definir clases en Python es con: class [Nombre de la clase]:
class Globo:
    #Para defininir su constructor se usa __init__ y como mínimo el parámetro self (Se refiere a la instancia del objeto)
    #Para llamar a un atributo de la instancia usamos self.[Nombre del atributo]
    #El parámetro self se puede llamar al gusto, pero es OBLIGATORIO
    def __init__(self,color,flota):
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
globo = Globo("Rojo", True)
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
        super().__init__(color, Flota) #Globo.__init__(self, color, Flota)
        #Podremos establecer otros atributos propios de la clase hijo
        self.tieneLuces = tieneLuces
    
    def Luces(self):
        if(self.tieneLuces):
            print("Soy un globo de fiesta con luces :D")
        else:
            print("Soy un globo de fiesta sin luces :(")
            
globoFiesta = GloboDeFiesta("Azul",False,True)
globoFiesta.Luces()