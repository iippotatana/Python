#1 Rappresentare la sequenza di valori: 3,4,5,"pippo",4.5
# in un set, in una lista, in una tupla.

valori = {3, 4, 5, "pippo", 4.5}
print(type(valori))
print(valori)

valori = list(valori)
print(type(valori))
print(valori)

valori = tuple(valori)
print(type(valori))
print(valori)
