# 24. En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una
# plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban
# apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo.
# A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera,
# con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse en
# cima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover
# los discos, llegaría el fn del mundo. Resolver este problema de la Torre de Hanói.

aguja_1 = []
aguja_2 = []
aguja_3 = []

for i in range(10):
    aguja_1.append(i)

def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.pop()
        destino.append(disco)
        return
    
    torre_hanoi(n - 1, origen, auxiliar, destino)
    disco = origen.pop()
    destino.append(disco)
    torre_hanoi(n - 1, auxiliar, destino, origen)


print(aguja_1)
print(aguja_2)
print(aguja_3)
torre_hanoi(10, aguja_1, aguja_3, aguja_2)
print(aguja_1)
print(aguja_2)
print(aguja_3)
