#4- Usando la funzione "input" chiedere all'utente di inserire due numeri, quindi comunicare all'utente
#se il secondo numero inserito è un multiplo del primo.

num1 = int(input("\nInserisci il primo numero: "))
num2 = int(input("\nInserisci il secondo numero: "))

if num2 % num1 == 0:
    print(f"\nIl numero {num2} è multiplo di {num1}\n")
else:
    print(f"\nIl numero {num2} non è multiplo di {num1}\n")

