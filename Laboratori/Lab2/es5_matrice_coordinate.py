#5 usando le strutture dati python che ritieni più opportune
#  rappresentare la seguente tabella di valori:

# 1 2 3
# 0 0 'pippo'
# 4 5 6

#nota: voglio cioè essere in grado di accedere ai valori in tabella
#"muovendomi" con un sistema di coordinate.
#Ad esempio l'elemento 'pippo' sarà accessibile usando coordinate
#2,1. 
#Riesci a farlo in più di un modo?

valori = [[1, 2, 3],
          [0, 0, "pippo"],
          [4, 5, 6]]

print(f"L'elemento che si trova in coordinate [1][2] è: {valori[1][2]}")


valori = {
    (0, 0): 1,
    (0, 1): 2,
    (0, 2): 3,
    (1, 0): 0,
    (1, 1): 0,
    (1, 2): "pippo",
    (2, 0): 4,
    (2, 1): 5,
    (2, 2): 6,
    }

print(f"L'elemento che si trova in coordinate [1][2] è: {valori[(1, 2)]}")
