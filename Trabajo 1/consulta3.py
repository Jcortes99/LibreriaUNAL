query3 = """
PREFIX bib: <http://localhost:8890/Biblioteca-Hemeroteca-Ludoteca/>
SELECT DISTINCT ?titulo ?editorial
WHERE {
  OPTIONAL {
    {?libr a bib:Prestado.}
    UNION
    { ?libr a bib:Disponible. }
  }
  ?libr bib:tieneTitulo ?titulo.
  ?libr bib:tieneEditorial ?editor.
  ?editor bib:tieneNombre ?editorial.
} ORDER BY ?editorial
"""
sparql.setQuery(query3)
results3 = sparql.query().convert()
# print(results3)
print("\n nombre y la editorial del libro:")
for result in results3["results"]["bindings"]:
    print(result["editorial"]["value"], result["titulo"]["value"]) 