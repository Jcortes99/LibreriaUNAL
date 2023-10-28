query1 = """
PREFIX bib: <http://localhost:8890/Biblioteca-Hemeroteca-Ludoteca/>
SELECT DISTINCT ?editorialNombre
WHERE {
  ?editor rdf:type bib:Editorial .
  ?editor bib:tieneNombre ?editorialNombre .
}
ORDER BY ?editorialNombre
"""
sparql.setQuery(query1)
sparql.setReturnFormat(JSON)
results1 = sparql.query().convert()

print("Editoriales en la ontología:")
for result in results1["results"]["bindings"]:
    print(result["editorialNombre"]["value"])