#3- Usando la funzione di python "input" chiedere all'utente di scrivere un numero intero.
# comunicare quindi all'utente se il numero scelto è pari e è dispari.

numero = int(input("\nInserisci un numero intero: "))

if numero % 2 == 0:
    print("\nIl numero inserito dall'utente è pari\n")
else:
    print("\nIl numero inserito dall'utente è dispari\n")
