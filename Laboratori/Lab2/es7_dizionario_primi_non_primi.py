#7 Chiedete all'utente un numero intero, formate quindi un dizionario
#con due chiavi: 'numeri primi', 'numeri non primi'.
#I valori associati alla prima chiave saranno tutti i numeri primi
#inferiori al numero intero scelto dall'utente, i valori associati
#alla seconda chiave saranno invece tutti i numeri non primi inferiori
#al numero scelto dall'utente.

numero_utente = int(input("Inserisci un numero intero: "))

dizionario = {"numeri_primi":[], "numeri_non_primi":[]}


for n in range(1, numero_utente):  
    is_primo = True
    
    for i in range(2, n): 
        if n % i == 0:    
            is_primo = False 
    if is_primo:   
        dizionario ["numeri_primi"].append(n)
    else:
        dizionario["numeri_non_primi"].append(n)


print(f"I numeri primi inferiori a: {numero_utente} sono: {dizionario["numeri_primi"]}")
print(f"I numeri NON primi inferiori a: {numero_utente} sono: {dizionario["numeri_non_primi"]}")
