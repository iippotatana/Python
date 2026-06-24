#8- Usando la funzione "input" chiedere all'utente di inserire un numero intero positivo: comunicare
#quindi all'utente se il numero inserito è un numero primo.
#ricorda: un numero (intero positivo) è primo se è divisibile solo per 1 e per se stesso, se cioè, non è multiplo
# di nessuno dei numeri positivi interi a lui inferiori 

numero = int(input("Inserisci un numero intero positivo: "))

is_primo = True

if numero <= 1:
    is_primo = False
else:
    for elenco in range(2, numero):
            if numero % elenco == 0:
                is_primo = False
                break
if is_primo:
    print("Il numero è primo")  
else:
    print("Il numero non è primo") 