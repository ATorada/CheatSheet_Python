#Fuente: https://www.bogotobogo.com/python/python_private_attributes_methods.php

class P:
   def __init__(self, nombre, alias):
      self.nombre = nombre  
      self.__alias = alias

   def who(self):
      print('Nombre  : ', self.nombre)
      print('Alias : ', self.__alias)
      
   def __foo(self):          # private method
      print('This is private method')

   def foo(self):            # public method
      print('This is public method')
      #self.__foo() Podemos llamar al método privado desde un método público


#Creación del objeto
p = P("Ángel","ATorada")

#Variables

print(p.nombre)
#print(p.__alias) Esto da error

#Se puede acceder, no es privado del todo.
print(p._P__alias)

#Métodos
p.foo()
#p.__foo() Esto da error
#Se puede acceder, no es privado del todo.
p._P__foo()