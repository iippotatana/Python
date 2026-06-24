#7- Assegnare ad una variabile una lista con elementi stringa, quindi selezionare solo gli elementi stringa
#con lunghezza inferiore a 4 caratteri e salvarli in una tupla eliminando gli eventuali doppioni.
#ricorda: la funzione "len()" restituisce la lunghezza di una stringa

lista = ["a3X", "mK2v9", "R7", "pL5sW", "jF4", "mK2v9","a3X"]

lista_finale = []
for elemento in lista: 
    if len(elemento) < 4:
        lista_finale.append(elemento)

lista_finale = tuple(set(lista_finale))

print(lista_finale)