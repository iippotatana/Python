#3 Scrivere un dizionario con 4 chiavi: "a","b","c","d"
# i valori associati alle chiavi saranno, rispettivamente, una lista,
#una tupla, un set, un dizionario. 
# (ci potete mettere dentro quello 
# che vi pare, anche altre strutture dati)

dizionario = {"a":["carta", "forbice", "sasso"],"b":("cuori", "picche", "fiori", "quadri"),"c":{"gennaio", "febbraio", "marzo"},"d":{"d1": (1, 2, 3), "d2":[4, 5, 6], "d3":{7, 8, 9}}}

print(dizionario["a"])
print(type(dizionario["a"]))
print()

print(dizionario["b"])
print(type(dizionario["b"]))
print()

print(dizionario["c"])
print(type(dizionario["c"]))
print()

print(dizionario["d"])
print(type(dizionario["d"]))
print()



