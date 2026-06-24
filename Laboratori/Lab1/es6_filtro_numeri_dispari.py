#6- Assegnare ad una variabile una lista con elementi numerici interi: estrarre da questa lista solo i numeri
#dispari, ed assegnarli tutti ad una nuova lista.

lista1 = [1, 2, 3, 4, 5, 6]
lista_dispari = []

for numero in lista1:
    if numero % 2 != 0:
        lista_dispari.append(numero)
        
print(lista_dispari)
    