#4 Scrivere una funzione che prenda input da terminale (quindi sempre 
# usando la funzione "input") e che si comporti come una calcolatrice.


def calcolatrice(a, b, operazione):
    if operazione == "+":
        return a + b
    elif operazione == "-":
        return a - b
    elif operazione == "*":
        return a * b
    elif operazione == "/":
        if b == 0:
            return f"Attenzione divisione per zero!!!"
        else:
            return a / b
        
op_input = input("\nInserisci l'operazione che vuoi eseguire? (+, -, *, /) o premi invio per spegnere la calcolatrice: ")

while op_input != "" :
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))


    print(f"Il risultato è: {calcolatrice(a, b, op_input)}")

    op_input = input("\nInserisci l'operazione che vuoi eseguire? (+, -, *, /) o premi invio per spegnere la calcolatrice: ")


print("Spegnimento in corso...")   