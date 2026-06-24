#1 Scrivere una funzione che prenda due argomenti numerici
#  e restituisca la somma, la sottrazione, il prodotto e la divisione
#  dei due numeri.

def operazioni(a,b):
    return a+b,a-b,a*b,a/b

a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))

print(operazioni(a,b))
print()

#Altra versione:

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
        

a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))

print(f"La somma di {a} e {b} è: {operazioni(a,b,somma = True)}")
print(f"La differenza di {a} e {b} è: {operazioni(a,b,differenza = True)}")
print(f"Il prodotto di {a} e {b} è: {operazioni(a,b,prodotto = True)}")
print(f"La divisione tra {a} e {b} è uguale a: {operazioni(a,b,divisione = True)}")