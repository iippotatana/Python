#9- Usando la funzione "input" chiedere all'utente di inserire un numero intero positivo: restituite all'utente
#la lista di tutti i numeri primi inferiori al numero indicato dall'utente.

numero = int(input("Inserisci un numero intero positivo:"))

numeri_primi = []

for n in range(2, numero): #Questo ciclo restituisce l'elenco di tutti i minori fino al numero inserito dall'utente. 
    is_primo = True
    
    for i in range(2, n): #Questo ciclo scorre i numeri minori.
        if n % i == 0:    #Verifico che i numeri minori siano divisibili solo per se stessi se trova pi
            is_primo = False
            break
    if is_primo:   
        numeri_primi.append(n)

print(f"I numeri primi inferiori al numero {numero} sono :{numeri_primi}")



