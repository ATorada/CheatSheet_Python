#Para hacer control de excepciones podemos usar las sentencias try: except:
try:
    print("Hola")
except:
    print("Error")
    
#Si queremos controlar una excepción en concreto simplemente tendremos que especificarla de la siguiente manera 

try:
    x = int(input("Please enter a number: "))
except ValueError: 
    #except (RuntimeError, TypeError, NameError) También se permite capturar más de una excepción en un mismo except
    #except BaseException as err: O añadir otros except (Al igual que es posible nombrar el error y posteriormente sacarlo por pantalla)
    print("Eso no es un numero")


#También se pueden realizar Throws de excepciones con la siguiente sentencia: raise NombreDelError('Mensaje')
#El error debe existir, aquí hay una lista https://docs.python.org/3/library/exceptions.html

try:
    raise EOFError('Error')
except EOFError as err:
    print("Se ha dado un error")
    print(err)
    
    
#También es importante recalcar que hay un apartado más en los try/except que es el Finally, este siempre se ejecuta al final del try catch (Al igual que el Else)

try:
  x > 3
except:
  print("Algo ha salido mal")
else:
  print("Nada ha ido mal")
finally:
  print("Ha acabado el try/except")