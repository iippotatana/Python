#2 Scrivere una funzione che prenda due argomenti stringa
# e che restituisce la conczione di queste due stringhe.

a = input("Inserisci la prima stringa: ")
b = input("Inserisci la seconda stringa: ")

def conc(a,b):
    return a + b

print(conc(a,b))