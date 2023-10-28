# Importar rdflib
#import elementos básicos de RDF
from rdflib import Literal, BNode, URIRef, Graph, Namespace
# Crear un grafo vacio
g = Graph()

# Cargar el grafo desde un archivo local en formato xml
g.parse("C:\\Users\\Usuario\\Documents\\University\\Recuperacion Web\\LibreriaUNAL\\LibreriaUnal.ttl", format="ttl")

consulta = """
PREFIX bib: <http://localhost:8890/Biblioteca-Hemeroteca-Ludoteca/>
SELECT DISTINCT ?editorialNombre
WHERE {
  ?editor rdf:type bib:Editorial .
  ?editor bib:tieneNombre ?editorialNombre .
}
ORDER BY ?editorialNombre
"""
for row in g.query(consulta):
    print(row.editorialNombre)