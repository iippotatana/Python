#6 usare la funzione input per permettere all'utente di usare python 
# come se fosse una classica calcolatrice:
#l'utente sceglierà che input_utente fare e su che valori calcolarla,
#visualizzerà quindi il risultato.
#nota: potete scegliere di scrivere una calcolatrice che si spegne 
# dopo ogni calcolo, oppure che si spegne solo quando vuole 
#l'utente: potrebbe essere utile un while con un break per far si
#che la calcolatrice continui a funzionare.

print("Benvenuto nell'app calcolatrice!")

while True:
    input_utente = input("Scegli un operazione o premi invio per spegnere: ")
    
    if input_utente == "":
        print("Spegnimento in corso ... Arrivederci!")
        break

    operazioni = ["+", "-", "*", "/"]
    
    if input_utente in operazioni:
        num1 = float(input("inserisci il primo numero: " ))
        num2 = float(input("inserisci il secondo numero: " ))
        
        if input_utente == "+":
            risultato = num1 + num2
        
        elif input_utente == "-":
            risultato = num1 - num2
        
        elif input_utente == "*":
            risultato = num1 * num2  

        elif input_utente == "/":
            if num2 == 0:
                print("\nATTENZIONE!!! Non puoi dividere un numero per zero.\n")
                continue
            else:
                risultato = num1 / num2

        print(f"Il risultato dell'operazione è: {risultato}")

    else:
        print("Hai inserito un operazione non valida!")







