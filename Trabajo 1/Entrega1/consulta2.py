query2 = """
PREFIX bib: <http://localhost:8890/Biblioteca-Hemeroteca-Ludoteca/>
SELECT DISTINCT ?autorNombre, ?paisOrigenLabel
WHERE {
  ?autor rdf:type bib:Autor .
  ?autor bib:añoDeNacimiento ?nacimiento .
  ?autor bib:tieneNombre ?autorNombre .
  FILTER(?nacimiento > 1900)
} ORDER BY ?autorNombre
"""
sparql.setQuery(query2)
results2 = sparql.query().convert()

print("\nAutores nacidos después de 1900:")
for result in results2["results"]["bindings"]:
    print(result["autorNombre"]["value"])