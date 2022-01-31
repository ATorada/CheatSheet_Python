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


print("movida")
shape = geom.create_shape(settings, ifcCasa.by_type("IfcWall")[0])
#print(ifcCasa.by_type("IfcWall")[0].get_info())
        # ios stands for IfcOpenShell
verts = shape.geometry.verts
ios_edges = shape.geometry.edges
faces = shape.geometry.faces
        # IfcOpenShell store vertices in a single tuple, same for edges and faces
print(len(verts))
print(ios_edges)
print("Caras")
print(faces)


grouped_verts = [[verts[i], verts[i + 1], verts[i + 2]] for i in range(0, len(verts), 3)]
grouped_faces = [[faces[i], faces[i + 1], faces[i + 2]] for i in range(0, len(faces), 3)]

print(grouped_faces)

print(grouped_verts)

import math
def distance(x1, y1, z1, x2, y2, z2):
      
    d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)
    return d
area = 0
for face in grouped_faces:
    d1 = distance(grouped_verts[face[0]][0],grouped_verts[face[0]][1],grouped_verts[face[0]][2],
            grouped_verts[face[1]][0],grouped_verts[face[1]][1],grouped_verts[face[1]][2])
    
    d2 = distance(grouped_verts[face[1]][0],grouped_verts[face[1]][1],grouped_verts[face[1]][2],
            grouped_verts[face[2]][0],grouped_verts[face[2]][1],grouped_verts[face[2]][2])

    d3 = distance(grouped_verts[face[0]][0],grouped_verts[face[0]][1],grouped_verts[face[0]][2],
            grouped_verts[face[2]][0],grouped_verts[face[2]][1],grouped_verts[face[2]][2])
    
    if (d1 > d2) and (d1 > d3):
        area += (d2 * d3)/2
    elif (d2 > d1) and (d2 > d3):
        area += (d1 * d3)/2
    else:
        area += (d2 * d1)/2
    
    print("Distancia1: " + str(d1) + " Distancia2: " + str(d2) + " Distancia3: " + str(d3))
print(area)