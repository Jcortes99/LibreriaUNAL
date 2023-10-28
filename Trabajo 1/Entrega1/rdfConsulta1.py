# Importar rdflib
#import elementos básicos de RDF
from rdflib import Literal, BNode, URIRef, Graph, Namespace
# Crear un grafo vacio
g = Graph()

# Cargar el grafo desde un archivo local en formato xml
g.parse("C:\\Users\\Usuario\\Documents\\University\\Recuperacion Web\\LibreriaUNAL\\LibreriaUnal.ttl", format="ttl")

consulta = """
PREFIX bib: <http://localhost:8890/Biblioteca-Hemeroteca-Ludoteca/>
SELECT DISTINCT ?socioNombre
WHERE {
  ?socio rdf:type bib:Socio .
  ?socio bib:tieneNombre ?socioNombre .
} ORDER BY ?socioNombre
"""
for row in g.query(consulta):
    print(row.socioNombre)