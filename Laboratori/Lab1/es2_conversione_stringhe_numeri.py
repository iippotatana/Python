#2- Gli stessi numeri convertiti in stringa del punto 1 ora li convertiamo di nuovo nel loro tipo originario: 
# ciò che era un numero intero torna intero, ciò che era un numero float torna float.


num1 = 126
num2 = 1936.27

num1 = str(num1)
num2 = str(num2)

print(f"\nIl primo numero è di tipo: ", type(num1))
print(f"Il secondo numero è di tipo: ", type(num2))

num1 = int(num1)
num2 = float(num2)

print(f"\nIl primo numero è di tipo: ", type(num1))
print(f"Il secondo numero è di tipo: ", type(num2))
print()