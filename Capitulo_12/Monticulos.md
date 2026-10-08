## Monticulos

Los monticulos en su base son arboles binarios

# Caracteristicas:

hay dos tipos: 
  - Monticulos Maximos: El padre es mayor que sus dos hijos
  - Monticulos Minimos: El padre es menor que sus dos hijos

Debe cumplir con la propiedad de ordenamiento

El arbol debe estar completo o casi completo, se completa de izquierda a derecha. (No se puede agregar un nivel sin que se complete el de arriba y no puede haber "huecos" entre niveles)


Se los puede representar como vectores/listas. Dentro del vector se encuentra los hijos (izquierdo o derecho) de un numero a travez de formulas, y de igual forma se encuentran los padres de un nodo


Para mantener el orden del arbol tras la insercion se una el mecanismo de flotar. De la misma forma, cuando se elimina un nodo se utiliza el hundir.

