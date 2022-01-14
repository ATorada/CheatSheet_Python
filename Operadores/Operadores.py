"""
~~ Practicando Operadores en Python~~
~~ Ángel Torada ~~
"""


#Los operadores en Python disponibles son:

# Arithmetic +,-,*,/,%,**(^), //
print(1+1)
print(2-1)
print(2*2)
print(4/2)
print(5%2)
print(2**2)
print(15//2)



# Reasignación =,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=
x = 5
x += 1  #6
x -= 1  #5
x *= 5  #25
x /= 5  #5
x %= 2  #1
x //= 1 #1
x **= 0 #1
#&= https://stackoverflow.com/questions/21237767/python-a-b-meaning 
#Es el AND binario
#|= Es el OR binario
#^= Es el XOR binario
#>>= Desplaza un Bit a la derecha
#<<= Desplaza un Bit a la izquierda




#Comparación ==, !=, >, <, >=, <=
print(str(1==1))
print(str(1!=1))
print(str(2>1))
print(str(2<1))
print(str(2>=2))
print(str(1<=2))

#Otros and, or, not, is, is not, in, not in
#and devuelve True si ambas son True x < 5 and  x < 10
#or devuelve True si uno de los dos es True x < 5 or x < 4
#not devuelve True si el resultado es False y False si el resultado es True not(x < 5 and x < 10)

#is devuelve si True si son el mismo tipo de OBJETO x is y
#is not devuelve si True si no son el mismo tipo de OBJETO x is y
#Disclaimer, si se usa == y se están comparando dos listas del mismo tamaño dará TRUE

#in devuelve True si X está en el objeto de Y tipo
#in devuelve True si X no está en el objeto de Y tipo

