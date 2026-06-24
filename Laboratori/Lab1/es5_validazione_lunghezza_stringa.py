#5- chiedere all'utente di scrivere un nome con massimo 5 lettere, se l'utente scrive un nome
#più lungo di 5 lettere noi gli chiediamo di nuovo di inserire un nome con massimo 5 lettere.
#ricorda: la funzione "len()" restituisce la lunghezza di una stringa

nome = input("\nInserisci un nikname con massimo 5 caratteri:")

while len(nome) > 5:
    nome = input("\nInserisci un nikname con massimo 5 caratteri:")

print("\nNickname inserito correttamente!\n")

