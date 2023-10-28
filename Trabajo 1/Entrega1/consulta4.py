query2 = """
PREFIX bib: <http://localhost:8890/Biblioteca-Hemeroteca-Ludoteca/>
SELECT DISTINCT ?socioNombre
WHERE {
  ?socio rdf:type bib:Socio .
  ?socio bib:tieneNombre ?socioNombre .
} ORDER BY ?socioNombre
"""
sparql.setQuery(query2)
results2 = sparql.query().convert()

print("\nSocios:")
for result in results2["results"]["bindings"]:
    print(result["socioNombre"]["value"])