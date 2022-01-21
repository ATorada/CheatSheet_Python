#Para instalarlo hay que ir a http://ifcopenshell.org/python
#Ahí descargar la versión e introducirla en site-packages (De nuestro python general) o en Lib (De nuestro entorno virtual)

import ifcopenshell as ifc

print(ifc.version)

#Abre un ifc
ifcCasa = ifc.open('C:\\Users\\Sabiin\\Downloads\\Proyecto1_Normal.ifc')

#Obtiene el atributo 1
print(ifcCasa.by_id(1))

#Obtenemos los muros de la casa
muros = ifcCasa.by_type("IfcWall")
print(len(muros)) #4 Cuantos hay
print(muros[0].is_a()) # IfcWallStandardCase Qué es el Muro1
print(muros[0].is_a("IfcWallStandardCase")) # True Es el Muro1 un IfcWallStandarCase

#Obtenemos el muro1
muro1 = muros[0]
#Mostramos su ID
print(muro1.id())
#Mostramos su primera propiedad
print(muro1[0])
#Mostramos todas sus propiedades (El texto que guardan)
for x in muro1:
    print(x)
#Obtenemos UNA propiedad en concreto del objeto
print(muro1.GlobalId)
#Obtenemos todas sus propiedades
print(muro1.get_info())

print()
products = ifcCasa.by_type('IfcProduct')
for product in products:
    print(product.is_a())

from ifcopenshell import geom
settings = geom.settings()

for ifc_entity in ifcCasa.by_type("IfcWall"):
    shape = geom.create_shape(settings, ifc_entity)
        # ios stands for IfcOpenShell
    ios_vertices = shape.geometry.verts
    ios_edges = shape.geometry.edges
    ios_faces = shape.geometry.faces
        # IfcOpenShell store vertices in a single tuple, same for edges and faces
print(ios_vertices)
print(ios_edges)
print(ios_faces)