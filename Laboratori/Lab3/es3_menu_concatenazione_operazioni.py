#3 Scrivere una funzione che prende input da utente (quindi dovrete
#usare la funzione di python "input") quindi, se l'utente vuole,
#  concatena le due stringhe immesse (ricorda: la funzione
# 'input' di python converte tutto in stringa ), oppure converte 
# le due stringhe #in numeri e replica l'output 
# della funzione del punto1.


a = input("\nInserisci la prima stringa: ")
b = input("\nInserisci la seconda stringa: ")
op = input("\nChe operazione vuoi eseguire? digita 1 per concatena 2 per operazioni matematiche invio per uscire:")

def conc(a,b):
    return a + b

def operazioni(a,b,somma = False,differenza = False, prodotto = False, divisione = False):
    if somma:
        return a + b
    elif differenza:
        return a - b
    elif prodotto:
        return a * b
    elif divisione:
        if b == 0:
            return None
        else:
            return a / b

while op != "":
    if op == "1":
        print(conc(a,b))
        
    elif op == "2":
        num_a = float(a)
        num_b = float(b)
        print(f"La somma di {a} e {b} è: {operazioni(num_a,num_b,somma = True)}")
        print(f"La differenza di {a} e {b} è: {operazioni(num_a,num_b,differenza = True)}")
        print(f"Il prodotto di {a} e {b} è: {operazioni(num_a,num_b,prodotto = True)}")
        print(f"La divisione tra {a} e {b} è uguale a: {operazioni(num_a,num_b,divisione = True)}")
    
    op = input("\nChe operazione vuoi eseguire? digita 1 per concatena 2 per operazioni matematiche invio per uscire:")

print("Spegnimento in corso...")
    
    
    
