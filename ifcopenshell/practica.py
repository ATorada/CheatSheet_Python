import ifcopenshell
from ifcopenshell import geom

print(ifcopenshell.version)

file = ifcopenshell.open('C:\\Users\\Sabiin\\Downloads\\Proyecto1_Normal.ifc')

print(file.by_type("IfcProject")[0]) #Proyecto, si no le ponemos el 0 sería una lista
proyecto = file.by_type("IfcProject")[0] #Lo guardamos

print(proyecto.IsDecomposedBy[0]) #En QUÉ se descompone
print(proyecto.IsDecomposedBy[0].RelatedObjects) #El Sitio del Proyecto
sitio = proyecto.IsDecomposedBy[0].RelatedObjects[0] #Lo guardamos

print(sitio.IsDecomposedBy[0]) #En QUÉ se descompone
print(sitio.IsDecomposedBy[0].RelatedObjects) #El Building del Sitio del Proyecto
building = sitio.IsDecomposedBy[0].RelatedObjects[0] #Lo guardamos

print(building.IsDecomposedBy[0]) #En QUÉ se descompone
print(building.IsDecomposedBy[0].RelatedObjects) #Los pisos de una construcción
pisos = building.IsDecomposedBy[0].RelatedObjects #Lo guardamos

print() #Muestro los 3 pisos del proyecto
print("Pisos")
for x in pisos:
    print(x)


#Cargo el piso que contiene una viga, en este caso el piso de nivel 0
piso0 = pisos[0]
print(piso0.get_info()) #Esto nos sirve para obtener la información en forma de diccionario
print(piso0.ContainsElements) #La relación que se encarga de relacionar los elementos con el piso
relacion_piso0 = piso0.ContainsElements[0] #Lo guardamos
productos_piso0 = relacion_piso0.RelatedElements #Guardamos los productor/elementos de nuestro piso
print(productos_piso0)

#Propiedades de la viga
viga = productos_piso0[0]
print("a")
#Todos los conjuntos de propiedades
for x in viga.IsDefinedBy:
    try:
        print(x.RelatingPropertyDefinition)
    except:
        print("Nada")

#Guardo el conjunto de  propiedades 1
print()
propiedad1 = viga.IsDefinedBy[1].RelatingPropertyDefinition
print("a")
print(viga.IsDefinedBy[1])
print("a")
print(propiedad1)
#Mostramos las propiedades del conjunto de propiedades 1
print(propiedad1.HasProperties)
print(propiedad1.HasProperties[1].Name)
print(propiedad1.HasProperties[1].NominalValue)
print(propiedad1.HasProperties[1].Unit)

#Cómo obtener los tipos de BuildingElements que tiene nuestro proyecto
#Building elements are all physically existent and tangible things
print()
print("Elementos de nuestro proyecto")
building_elements = set()

for x in file.by_type("IfcRoot"):
    if x.is_a("IfcBuildingElement"):
        building_elements.add(x)

for nombre in building_elements:
    print(nombre.is_a())




count = 0
for element in file.by_type("IfcDoor")[0].IsDefinedBy:
    try:
        print(element.RelatingPropertyDefinition.HasProperties)
    except:
        print()

print(count)

import ifcopenshell.util.element




print(ifcopenshell.util.element.get_psets(file.by_type("IfcDoor")[0])['Pset_DoorCommon'])

for x in ifcopenshell.util.element.get_psets(file.by_type("IfcDoor")[0]):

    print()
    for y in ifcopenshell.util.element.get_psets(file.by_type("IfcDoor")[0])[x]:
        print(x +" " + y)

print("Movida")

for key, pset in ifcopenshell.util.element.get_psets(file.by_type("IfcDoor")[0]).items():
    
    print("         --- "+key + " --- ")
    print()
    for keypset, value in pset.items():
        print("  "+keypset)
        print("    * " + str(value) )
    print()
    
print(ifcopenshell.util.element.get_container(file.by_type("IfcDoor")[0]))

print(file.by_type("IfcDoor")[0].get_info())